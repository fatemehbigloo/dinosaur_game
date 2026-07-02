# dinosaur_game
A game-making robot that detects obstacles in a dinosaur game by taking a screenshot of the screen and automatically jumps! It stops by pressing the Q key. 🦕


📄 README - Chrome Dino Game Bot

Bookmark
# 🦕 Chrome Dino Bot - Automatic Dinosaur Game Bot
A simple bot that uses machine vision and screenshots to automatically play the Google Dinosaur game and when it detects (cacti or birds), it does so.

## 🎯 Usage
This bot is made for education and entertainment and shows how to work with the libraries:
- ``Pythogi'' (keyboard and mouse simulation)
- ``PIL'' (image processing)
- ``Keyboard'' (user input input)

## 📋 Prerequisites
- Python 3.6 or higher
- Operating system: Windows / Linux / macOS
- Chrome browser with Dino game open (chrome://dino)Automatic obstacle detection and control of dinosaur game Description:
Disconnect your internet and open Chrome browser. When you try to open this web page, it will show you the dinosaur game which starts when you press the space bar. Write a program that advances this game by one night for every day. Tutorial key

🚀 How to run
1. Open the Chrome browser and go to the following address:
chrome://dino
2. Start the game (the dinosaur must be running).
3. Run the program:
bash
python dino_bot.py
4. Wait 3 seconds for the robot to prepare and it will automatically start playing.
5. To stop the robot, press the Q key.

📁 Project structure
Explanation file
dino_bot.py Main program file

⚙️ How it works
1. Specify the scan area
python
SEARCH_AREA = (700, 380, 827, 400)
These coordinates specify the area that the robot will scan to detect obstacles.

⚠️ Important Notes
· Make sure the dinosaur game is open on the screen and running.
· If your screen coordinates are different from my device, adjust the value of SEARCH_AREA.
· To find the exact coordinates, use tools like pyautogui.position().
· The robot may be a little weak in recognizing birds (due to their small size).
· Make sure the Chrome window is active before running.

🧪 Testing and debugging
If the robot doesn't work:
1. Check the SEARCH_AREA coordinates (it should stop the dinosaur).
2. Make sure the game is not in Dark Mode (colors are different).
3. Set the screen resolution to 100% (no zoom).
4. Test the detection by printing bg_color and the color of the obstacles.

👨‍💻 Developer
[fatemeh bigloo] - [ghasembigloo5@gmail.com]
