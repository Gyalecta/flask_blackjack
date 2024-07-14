# Blackjack Web App

This is a simple web application for playing Blackjack, built using Python (Flask), HTML, CSS, and JavaScript.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a basic implementation of the Blackjack game. The game is played against the computer dealer, following the standard rules of Blackjack. The application is designed to be user-friendly with a clean interface.

## Features

- Play a complete game of Blackjack
- Simple and intuitive user interface
- Dealer AI for automated game flow
- Responsive design for various screen sizes

## Installation

To run this application locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gyalecta/flask_blackjack.git
   cd flask_blackjack
   ```

2. **Set up a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   flask run
   ```
   The application will be accessible at `http://127.0.0.1:8080`.

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:8080`.
2. Start a new game by clicking the "New Game" button.
3. Use the "Hit" button to draw a card, or the "Stand" button to hold your total.
4. The dealer will automatically play after you stand.
5. The result of the game will be displayed, and you can start a new game by clicking "New Game" again.

## Technologies Used

- **Python:** Backend logic using Flask framework
- **HTML:** Structure of the web pages
- **CSS:** Styling of the web pages
- **JavaScript:** Frontend logic and interactions

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a pull request

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
