import os
import argparse
from moviepy.editor import VideoFileClip, concatenate_videoclips

def combine_media_files(input_files, output_file):
    clips = []
    for file in input_files:
        if not os.path.exists(file):
            print(f"Error: File {file} does not exist.")
            return
        clip = VideoFileClip(file)
        clips.append(clip)
    
    if not clips:
        print("No valid media files provided.")
        return
    
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
    print(f"Media files have been successfully combined into {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Combine multiple media files into one.")
    parser.add_argument('input_files', nargs='+', help='List of input media files to combine.')
    parser.add_argument('--output', required=True, help='Output file name for the combined media.')
    args = parser.parse_args()

    combine_media_files(args.input_files, args.output)

if __name__ == "__main__":
    main()