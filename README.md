# Assistive Glasses for Deaf Individuals

An AI-powered assistive technology solution that provides real-time speech-to-text conversion and environmental sound awareness for deaf and hard-of-hearing individuals.

## Project Overview

This project aims to develop smart glasses that:
- Convert spoken language to text displayed in the user's field of view
- Provide directional awareness of sounds through haptic feedback
- Manage group conversations with speaker identification
- Implement context-aware text abbreviation for faster reading
- Store conversation history with quick summarization
- Recognize environmental sounds and alerts

## Repository Structure

- `/docs` - Documentation for hardware, software, and user guides
- `/firmware` - Embedded software for the glasses hardware
- `/mobile_app` - Companion mobile application
- `/tools` - Development utilities and scripts
- `/ml_training` - Machine learning model training and evaluation
- `/prototypes` - Early prototype implementations

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 14+ (for mobile app)
- Required Python packages: see `requirements.txt`

### Setting Up Development Environment

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/assistive-glasses.git
   cd assistive-glasses
   ```

2. Set up Python environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up mobile app development environment
   ```bash
   cd mobile_app
   npm install
   # or if using yarn
   yarn install
   ```

## Development Roadmap

- [x] Repository setup and project structure
- [ ] Basic speech recognition implementation
- [ ] Display interface development
- [ ] Mobile app Bluetooth connectivity
- [ ] Context-aware text processing
- [ ] Directional audio detection
- [ ] Haptic feedback system
- [ ] Group conversation management
- [ ] Environmental sound recognition
- [ ] Integration and system testing

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

## Acknowledgments

- List any libraries, resources, or individuals that have been instrumental to your project
