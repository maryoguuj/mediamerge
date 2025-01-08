# MediaMerge

MediaMerge is a simple command-line tool designed to combine multiple media files into a single optimized file on Windows platforms. It leverages the power of [MoviePy](https://zulko.github.io/moviepy/) to handle various media formats efficiently.

## Features

- Combine multiple video files into one.
- Supports various video formats like MP4, AVI, etc.
- Optimizes the output for smooth playback.

## Requirements

- Python 3.6 or above
- MoviePy
- ImageIO[ffmpeg]

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/MediaMerge.git
    cd MediaMerge
    ```

2. Install the required packages:
    ```bash
    pip install moviepy imageio[ffmpeg]
    ```

## Usage

To combine media files, use the following command:

```bash
python media_merge.py input1.mp4 input2.mp4 --output output.mp4
```

Replace `input1.mp4`, `input2.mp4`, etc., with the paths to your media files, and `output.mp4` with your desired output file name.

## Example

```bash
python media_merge.py video1.mp4 video2.mp4 video3.mp4 --output combined_video.mp4
```

This command will merge `video1.mp4`, `video2.mp4`, and `video3.mp4` into a single file named `combined_video.mp4`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.