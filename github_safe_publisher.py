#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
=========================================================
GITHUB SAFE PUBLISHER
Author: Gonzalo De la Rivera (Godear24)
Purpose: Prevent GitHub rate-limit / blocks when working
         with high-output AI systems (Manus, LLMs, agents)
=========================================================

WHAT THIS DOES:
- Publishes content to GitHub in HUMAN-LIKE batches
- Avoids rapid-fire commits
- Protects against GitHub abuse detection
- Designed for AI-assisted creation pipelines

WORKFLOW:
IA / Manus → local buffer → READY_TO_PUBLISH → this script → GitHub

USAGE:
1. Put files you want to publish inside ./READY_TO_PUBLISH
2. Run: python github_safe_publisher.py
3. Script commits + pushes safely

CONFIGURATION:
- COMMITS_PER_RUN: How many commits per execution (default: 1)
- DELAY_BETWEEN_RUNS: Wait time between commits (default: 1 hour)
- MAX_FILES_PER_COMMIT: Max files per single commit (default: 30)

EXAMPLE WORKFLOW:
1. AI generates 100 files
2. All go to ./READY_TO_PUBLISH
3. Run: python github_safe_publisher.py
4. Script publishes 1 commit with up to 30 files
5. Waits 1 hour
6. Next run publishes next batch
7. No GitHub blocks, no rate limits

This allows high-output AI systems to safely contribute
to GitHub without triggering abuse detection.
"""

import os
import time
import subprocess
from datetime import datetime
import sys

# ==========================
# CONFIGURATION
# ==========================

READY_DIR = "READY_TO_PUBLISH"
COMMITS_PER_RUN = 1          # safe default: 1 commit per run
DELAY_BETWEEN_RUNS = 60 * 60 # 1 hour between commits
MAX_FILES_PER_COMMIT = 30     # max files per commit

COMMIT_PREFIX = "docs: batch publish"
LOG_FILE = "publisher.log"

# ==========================
# UTILS
# ==========================

def log(msg):
    """Log to console and file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {msg}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def run(cmd):
    """Run shell command and return result"""
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    except subprocess.TimeoutExpired:
        log(f"Command timeout: {' '.join(cmd)}")
        return None
    except Exception as e:
        log(f"Command error: {e}")
        return None

def check_git_status():
    """Verify we're in a git repository"""
    result = run(["git", "status"])
    if result is None or result.returncode != 0:
        log("ERROR: Not in a git repository or git not available")
        return False
    return True

# ==========================
# CORE LOGIC
# ==========================

def get_files():
    """Get all files from READY_TO_PUBLISH directory"""
    if not os.path.exists(READY_DIR):
        os.makedirs(READY_DIR)
        log(f"Created {READY_DIR} directory")
        return []
    
    files = []
    for root, _, filenames in os.walk(READY_DIR):
        for name in filenames:
            if not name.startswith('.'):  # ignore hidden files
                files.append(os.path.join(root, name))
    
    return sorted(files)

def publish_batch(files):
    """
    Publish a batch of files in a single commit
    Returns True if successful, False otherwise
    """
    if not files:
        return False
    
    # Select files for this commit
    selected = files[:MAX_FILES_PER_COMMIT]
    
    log(f"Publishing {len(selected)} files...")
    
    # Stage files
    for f in selected:
        result = run(["git", "add", f])
        if result is None or result.returncode != 0:
            log(f"Warning: Could not add {f}")
    
    # Create commit
    message = f"{COMMIT_PREFIX} ({len(selected)} files) - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    commit = run(["git", "commit", "-m", message])
    
    if commit is None:
        log("ERROR: Commit command failed")
        return False
    
    if "nothing to commit" in commit.stdout.lower():
        log("Nothing to commit (no changes)")
        return False
    
    # Push to remote
    push = run(["git", "push", "origin", "main"])
    
    if push is None or push.returncode != 0:
        log(f"ERROR: Push failed")
        if push:
            log(f"  stdout: {push.stdout}")
            log(f"  stderr: {push.stderr}")
        return False
    
    log(f"✓ Successfully published batch: {message}")
    
    # Remove published files from buffer
    for f in selected:
        try:
            os.remove(f)
            log(f"  Removed: {f}")
        except Exception as e:
            log(f"  Warning: Could not remove {f}: {e}")
    
    return True

def wait_for_next_batch():
    """Wait between batches to simulate human rhythm"""
    hours = DELAY_BETWEEN_RUNS / 3600
    log(f"Waiting {hours:.1f} hours before next batch...")
    time.sleep(DELAY_BETWEEN_RUNS)

# ==========================
# EXECUTION
# ==========================

def main():
    """Main execution loop"""
    log("=" * 60)
    log("GitHub Safe Publisher started")
    log("=" * 60)
    
    # Check git status
    if not check_git_status():
        sys.exit(1)
    
    # Get files to publish
    files = get_files()
    
    if not files:
        log("No files to publish in READY_TO_PUBLISH/")
        log("Workflow: Generate files → Move to READY_TO_PUBLISH/ → Run this script")
        sys.exit(0)
    
    log(f"Found {len(files)} files to publish")
    
    commits_done = 0
    
    while files and commits_done < COMMITS_PER_RUN:
        success = publish_batch(files)
        
        if not success:
            log("Batch publish failed, stopping")
            break
        
        commits_done += 1
        files = get_files()
        
        if files and commits_done < COMMITS_PER_RUN:
            wait_for_next_batch()
    
    log("=" * 60)
    log(f"Publisher finished. Published {commits_done} batch(es)")
    log("=" * 60)

if __name__ == "__main__":
    main()
