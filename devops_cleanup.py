#!/usr/bin/env python3
"""
DevOps Repository Cleanup Script
===============================

Clean up the DevOps repository by:
1. Removing duplicate/backup files
2. Organizing video files
3. Consolidating HTML files
4. Archiving unused scripts
5. Creating a clean professional structure

Author: Hubert Kozuchowski
"""

import os
import shutil
from datetime import datetime

class DevOpsRepoCleanup:
    """Clean up DevOps repository for professional presentation"""
    
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.archive_dir = f"archived_cleanup_{self.timestamp}"
        
        # Files to keep (essential/production)
        self.keep_files = {
            'index.html',  # Main portfolio
            'Hubert-Kozuchowski.html',  # Main resume
            'GROK_AI_APPLICATION_README.md',  # Documentation
            '.git',  # Git repository
            '.github'  # GitHub configuration
        }
        
        # Files to remove (duplicates/backups)
        self.remove_files = {
            'Hubert-Kozuchowski-backup.html',
            'Hubert-Kozuchowski-backup-before-video-removal.html',
            'index_backup.html',
            'index_with_video_backup.html',
            'remove_video_final.py',
            'remove_video_from_main.py',
            'remove_video_from_resume.py',
            'fix_resume.py'
        }
        
        # Video files to evaluate
        self.video_files = {
            'epic-linkedin-video.mp4',
            'GROK_12SEC_EPIC_FULL_EPIC_SEQUENCE.mp4'
        }
        
        # Project files to organize
        self.project_files = {
            'grok-ai-job-application.html',
            'linkedin-epic-project.html',
            'viral-epic-campaign.html',
            'viral_campaign_builder.py'
        }
    
    def create_archive_dir(self):
        """Create archive directory"""
        os.makedirs(self.archive_dir, exist_ok=True)
        print(f"✅ Created archive directory: {self.archive_dir}/")
    
    def remove_backup_files(self):
        """Remove backup and duplicate files"""
        print(f"\n🗑️ Removing backup and duplicate files...")
        
        removed_count = 0
        for file in self.remove_files:
            if os.path.exists(file):
                # Move to archive instead of deleting
                shutil.move(file, os.path.join(self.archive_dir, file))
                print(f"   📦 Archived: {file}")
                removed_count += 1
        
        print(f"📊 Archived {removed_count} backup/duplicate files")
    
    def organize_video_files(self):
        """Handle video files - move to archive or keep based on size/relevance"""
        print(f"\n🎥 Organizing video files...")
        
        video_count = 0
        for video in self.video_files:
            if os.path.exists(video):
                # Check file size
                size_mb = os.path.getsize(video) / (1024 * 1024)
                
                if size_mb > 10:  # Large videos archive
                    shutil.move(video, os.path.join(self.archive_dir, video))
                    print(f"   📦 Archived large video: {video} ({size_mb:.1f}MB)")
                else:
                    print(f"   ✅ Keeping small video: {video} ({size_mb:.1f}MB)")
                video_count += 1
        
        print(f"📊 Processed {video_count} video files")
    
    def organize_project_files(self):
        """Organize project-specific files into subdirectory"""
        print(f"\n📁 Organizing project files...")
        
        projects_dir = "projects"
        if not os.path.exists(projects_dir):
            os.makedirs(projects_dir, exist_ok=True)
        
        organized_count = 0
        for project_file in self.project_files:
            if os.path.exists(project_file):
                shutil.move(project_file, os.path.join(projects_dir, project_file))
                print(f"   📁 Moved to projects/: {project_file}")
                organized_count += 1
        
        print(f"📊 Organized {organized_count} project files")
    
    def create_clean_readme(self):
        """Create a clean professional README"""
        readme_content = """# DevOps Professional Portfolio

## 🚀 Hubert Kozuchowski - Senior DevOps Engineer

Professional DevOps portfolio showcasing automation tools, infrastructure solutions, and cloud expertise.

### 📊 Portfolio Contents

- **🏠 index.html** - Professional portfolio homepage
- **📄 Hubert-Kozuchowski.html** - Comprehensive professional resume
- **📁 projects/** - Specialized project demonstrations
- **📚 GROK_AI_APPLICATION_README.md** - Project documentation

### 🎯 Expertise Areas

- ☁️ **Cloud Infrastructure** - AWS, Azure, GCP
- 🚀 **DevOps Automation** - CI/CD, Infrastructure as Code
- 🐳 **Containerization** - Kubernetes, Docker
- 📊 **Monitoring & Observability** - Prometheus, Grafana
- 🔧 **Automation Tools** - Terraform, Ansible, Python

### 🛠️ Professional Projects

- **LinkedIn Job Search Automation** - AI-powered job application system
- **Cloud Infrastructure Optimization** - 40% cost reduction, 80% faster deployments
- **CI/CD Pipeline Implementation** - Serving 100+ developers
- **Kubernetes Cluster Management** - 1M+ requests daily, 99.9% uptime

### 📞 Contact

- **📧 Email:** hubert.kozuchowski@devops.com
- **💼 LinkedIn:** [linkedin.com/in/hubert-kozuchowski](https://linkedin.com/in/hubert-kozuchowski)
- **🐙 GitHub:** [github.com/kozuchowskihubert](https://github.com/kozuchowskihubert)

---

*Professional DevOps Engineer specializing in cloud infrastructure and automation*

**Repository cleaned and organized:** {datetime.now().strftime('%B %d, %Y')}
"""
        
        with open('README.md', 'w') as f:
            f.write(readme_content)
        
        print("✅ Created clean professional README.md")
    
    def create_gitignore(self):
        """Create professional .gitignore"""
        gitignore_content = """# DevOps Portfolio .gitignore
# Professional repository - hide development artifacts

# Archive directories
archived_*
backup_*
old_*

# Development files
*.log
*.tmp
*.temp
.DS_Store
*.pyc
__pycache__/

# Large media files
*.mp4
*.mov
*.avi

# Personal data
credentials.json
config.json
*.key
*.pem

# IDE files
.vscode/
.idea/
*.swp

# Professional portfolio - keep only production files visible
"""
        
        with open('.gitignore', 'w') as f:
            f.write(gitignore_content)
        
        print("✅ Created professional .gitignore")
    
    def show_final_structure(self):
        """Show final clean repository structure"""
        print(f"\n🎉 DEVOPS REPOSITORY CLEANUP COMPLETE!")
        print(f"=" * 60)
        
        print(f"📁 Clean Repository Structure:")
        for item in sorted(os.listdir('.')):
            if not item.startswith('.') and not item.startswith('archived_'):
                if os.path.isdir(item):
                    print(f"   📁 {item}/")
                    # Show contents of subdirectories
                    try:
                        for subitem in sorted(os.listdir(item)):
                            if not subitem.startswith('.'):
                                print(f"      📄 {subitem}")
                    except:
                        pass
                else:
                    if item.endswith('.html'):
                        emoji = '🌐'
                    elif item.endswith('.md'):
                        emoji = '📚'
                    elif item.endswith('.py'):
                        emoji = '🐍'
                    else:
                        emoji = '📄'
                    print(f"   {emoji} {item}")
        
        print(f"\n📦 Archived Content: {self.archive_dir}/")
        
        print(f"\n✨ Professional Repository Ready:")
        print(f"   🏠 Clean portfolio homepage")
        print(f"   📄 Professional resume")
        print(f"   📁 Organized project files")
        print(f"   📚 Comprehensive documentation")
        print(f"   🔒 Professional .gitignore")
        
        print(f"\n🌐 Portfolio URLs:")
        print(f"   • https://kozuchowskihubert.github.io/DevOps/")
        print(f"   • https://kozuchowskihubert.github.io/DevOps/Hubert-Kozuchowski.html")
    
    def run_cleanup(self):
        """Execute complete repository cleanup"""
        print(f"🧹 DevOps Repository Professional Cleanup")
        print(f"=" * 50)
        print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🎯 Goal: Create clean professional DevOps portfolio")
        print(f"=" * 50)
        
        # Create archive directory
        self.create_archive_dir()
        
        # Remove backup files
        self.remove_backup_files()
        
        # Organize video files
        self.organize_video_files()
        
        # Organize project files
        self.organize_project_files()
        
        # Create clean documentation
        self.create_clean_readme()
        
        # Create professional gitignore
        self.create_gitignore()
        
        # Show final structure
        self.show_final_structure()
        
        return True

def main():
    """Main execution"""
    cleaner = DevOpsRepoCleanup()
    cleaner.run_cleanup()

if __name__ == "__main__":
    main()