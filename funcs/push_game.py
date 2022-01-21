from random import choice, randrange

from discord.embeds import Embed

def getDist(pt1, pt2):
    return ((pt1[0] - pt2[1]) ** 2 + (pt1[1] - pt2[1]) ** 2) ** .5


class PushGame:

    BORDER_SYMBOLS = ['⬜', '🟪', '🟧', '☮', '⛔', '☢']
    BOX_SYMBOLS = ['🟫', '🟫', '🟫', '🟫', '🟫', '💎', '💿', '❤', '🧡', '💛', '💚', '💙', '💜', '🤎', '🤍', '🌚', '⭐']

    def __init__(self):
        self.level = 1
        self.boxes = 1
        self.map_size = 8
        self.obstacles = 0
        self.boxes = 1
        self.currMap = []
        self.border_symbol = ''
        self.box_symbol = ''
        self.playerX = 0
        self.playerY = 0
        self.goalX = 0
        self.goalY = 0
        self.score = 0
        self.resetMap()
        self.newLevel()
        
        
    def resetMap(self):
        # generates 8 x 8 map
        self.currMap = []
        for iter in range(self.map_size):
            temp_row = []
            for inner_iter in range(self.map_size):
                if iter == 0 or inner_iter == 0 or iter == self.map_size - 1 or inner_iter == self.map_size - 1:
                    temp_row.append('border')
                else:
                    temp_row.append('empty')
                    
            self.currMap.append(temp_row)
    
                
    def newLevel(self):
        self.border_symbol = choice(PushGame.BORDER_SYMBOLS)
        self.box_symbol = choice(PushGame.BOX_SYMBOLS)
        self.map_size = 8 + int(self.level / 4)
        self.boxes = 1 + int(self.level / 5)

        self.resetMap()
        player_pos = [randrange(1, self.map_size - 1), randrange(1, self.map_size - 1)]

        self.playerY = player_pos[0]
        self.playerX = player_pos[1]
        self.currMap[player_pos[0]][player_pos[1]] = 'player'

        new_goal = []
        overlap = True
        
        while overlap:
            new_goal = [randrange(1, self.map_size - 1), randrange(1, self.map_size - 1)]
            if new_goal != player_pos:
                overlap = False

        self.currMap[new_goal[0]][new_goal[1]] = 'goal'

        
        new_boxes = []
        for iter in range(self.boxes):
            new_box = []
            overlap = True

            while overlap:
                new_box = [randrange(2, self.map_size - 2), randrange(2, self.map_size - 2)]
                overlap = False
                if len(new_boxes) == 0:
                    if new_box == new_goal or new_box == player_pos:
                        overlap = True
                else:
                    for box in new_boxes:
                        if getDist(new_box, box) <= 1 or new_box == new_goal or new_box == player_pos:
                            overlap = True
                            break
                        else:
                            pass
            
            new_boxes.append(new_box)
                    
        for box in new_boxes:
            self.currMap[box[0]][box[1]] = 'box'
        
                
    def update(self, direction):
        self.score -= 1
        if self.score < 0:
            self.score = 0
        deltaX = 0
        deltaY = 0
        if direction == 'up':
            deltaY = -1
        elif direction == 'down':
            deltaY = 1
        elif direction == 'right':
            deltaX = 1
        elif direction == 'left':
            deltaX = -1
        
        dest = self.currMap[self.playerY + deltaY][self.playerX + deltaX]
        
        if dest == 'border':
            pass
        elif dest == 'goal':
            pass
        elif dest == 'box':

            if self.currMap[self.playerY + 2 * deltaY][self.playerX + 2 * deltaX] == 'goal':
                self.currMap[self.playerY][self.playerX] = 'empty'
                self.currMap[self.playerY + deltaY][self.playerX + deltaX] = 'player'
                self.playerX += deltaX
                self.playerY += deltaY

            elif self.currMap[self.playerY + 2 * deltaY][self.playerX + 2 * deltaX] == 'empty':
                self.currMap[self.playerY][self.playerX] = 'empty'
                self.currMap[self.playerY + deltaY][self.playerX + deltaX] = 'player'
                self.currMap[self.playerY + 2 * deltaY][self.playerX + 2 * deltaX] = 'box'
                self.playerX += deltaX
                self.playerY += deltaY
                
        else:
            self.currMap[self.playerY][self.playerX] = 'empty'
            self.currMap[self.playerY + deltaY][self.playerX + deltaX] = 'player' 
            self.playerX += deltaX
            self.playerY += deltaY
        
        

        win = True
        for row in self.currMap:
            for element in row:
                if element == 'box':
                    win = False
                    break
        if win:
            self.win()

    def win(self):
        
        self.level += 1
        self.score += self.level * 10
        self.newLevel()


    def Renderer(self):
        output_text = ''
        
        for row in self.currMap:
            for element in row:
                if element == 'player':
                    output_text += '😳'
                elif element == 'border':
                    output_text += self.border_symbol
                elif element == 'empty':
                    output_text += '⬛'
                elif element == 'goal':
                    output_text += '🟩'
                elif element == 'box':
                    output_text += self.box_symbol
            output_text += '\n'
            
        embed=Embed(title="**推箱子**")
        embed.set_thumbnail(url="https://i.imgur.com/w8f5M8q.png")
        embed.add_field(name="```目前關卡```", value=f'*{str(self.level)}*', inline=True)
        embed.add_field(name="```每關箱子```", value=f'*{str(self.boxes)}*', inline=True)
        embed.add_field(name="```地圖大小```", value=f'*{str(self.map_size)}*', inline=True)
        embed.add_field(name="```目前分數```", value=f'*{str(self.score)}*', inline=True)
        embed.add_field(name="遊戲畫面", value=output_text, inline=False)

        
        return embed
