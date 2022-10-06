# Game-of-life
A simple but fun game for two players, based on [Conway's Game of life](https://en.wikipedia.org/wiki/Conway's_Game_of_Life).  
The game is suitable for all ages and its duration is up to players' discretion.  
This is not an online game, both palyers should have access to the computer running the program.

### Instructions:
1. Install python version 3, if you haven't already. **Python 3.7** or later is recommended. The game uses the default graphics library [tkinter](https://docs.python.org/3/library/tkinter.html) and you don't have to install any additional libraries.
2. Download both the python script (Game_of_Life.py) and the icon (img.ico). Make sure to place them in the same directory.
3. Launch the python script. The settings screen pops-up. Feel free to customize your game. Availiable adjustments include:
    - **name and color of the players.** For display purposes only.
    - **Grid size**, measured in number of rectangles. (Width **X** Height). It is advised to choose a square grid.
    - **number of moves** for each player, i.e. number of shells they can place during their turn.
    - **number of iterations**, i.e. number of steps in time that will be executed to determine how many shells survive
4. Once you are ready, click on the **"Let's play!" button** or hit enter on your keyboard. That settings menu will be closed and the main program will start. The player who plays first is randomly defined. You can see whose player's turn it is on the top right corner.
5. The program has two control buttons on the bottom left corner: 
    - Click on the first button or hit "Esc" on your keyboard, whenever you want to **close the app**.
    - Click on the second button or hit "ctrl" on your keyboard, if you want to **re-customize your game** and start over.

### How to play:
During your turn, **left click on a square of the grid to place a shell**. That counts as one move. If you change your mind, click on that square again to remove it.
When you finish all your moves, click on "End turn". The program will automatically perform the predefined number of iterations. The number of shells per iteration is determined according to Conway's rules:
> Any live cell with fewer than two live neighbours dies, as if by underpopulation.  
> Any live cell with two or three live neighbours lives on to the next generation.  
> Any live cell with more than three live neighbours dies, as if by overpopulation.  
> Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.  

If you want more information read the [wikipedia article](https://en.wikipedia.org/wiki/Conway's_Game_of_Life) or [try the game online](https://playgameoflife.com/).  

In the screen, only the shells alive in the last iteration will be displayed. After about 2 seconds, the other palyer's turn will start.

### Tips:
- try to place your moves sensibly. Your goal is to have as many colored blocks as possible after the iterations, so that you get more points.
- be creative. Probably you can create a beautiful shape with your squares.
- be quick. The faster you play your moves, the better score you will get.

Any question or feedback is welcome.
