#!/usr/bin/env python3
"""
Fix resume page with epic video integration
"""
import re

def fix_resume_page():
    print("📋 Fixing resume page with epic video...")
    
    with open('Hubert-Kozuchowski.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Epic professional video section for resume
    resume_video_section = '''
    <!-- 🔥 EPIC PROFESSIONAL VIDEO SHOWCASE 🔥 -->
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; margin: 20px 0; border-radius: 15px; text-align: center; color: white; box-shadow: 0 10px 25px rgba(0,0,0,0.2);">
        <h2 style="color: #fff; margin-bottom: 15px;">🎬 INNOVATIVE AI PROJECT SHOWCASE</h2>
        <p style="margin-bottom: 20px; font-size: 16px;">Demonstrating Creative Problem-Solving & AI Integration Skills</p>
        
        <div style="max-width: 600px; margin: 0 auto;">
            <video controls style="width: 100%; border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.3);">
                <source src="GROK_12SEC_EPIC_FULL_EPIC_SEQUENCE.mp4" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
        
        <div style="margin-top: 20px;">
            <h3 style="color: #fff;">🔥 Epic AI-Powered Recruitment Strategy</h3>
            <p style="margin: 10px 0;">Created using Grok AI with custom "Swim in molten lava and HA HA" soundtrack integration</p>
            
            <div style="display: flex; justify-content: space-around; margin-top: 15px; flex-wrap: wrap;">
                <div style="margin: 5px;">
                    <strong>🤖 Technology:</strong><br>
                    Grok AI, FFmpeg, Python
                </div>
                <div style="margin: 5px;">
                    <strong>🎯 Purpose:</strong><br>
                    Innovation in recruitment
                </div>
                <div style="margin: 5px;">
                    <strong>📈 Result:</strong><br>
                    Viral potential achieved
                </div>
            </div>
        </div>
    </div>
'''
    
    # Find the container div and inject right after it
    container_pattern = r'(<div class="container">)'
    if re.search(container_pattern, content):
        content = re.sub(container_pattern, r'\1' + resume_video_section, content)
        print("✅ Epic video section injected into resume!")
    else:
        print("❌ Could not find container in resume")
        return False
    
    # Write updated content
    with open('Hubert-Kozuchowski.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

if __name__ == "__main__":
    fix_resume_page()