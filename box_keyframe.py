"""
A program where you click and then you press f to make the targets
"""
import pygame
win = pygame.display.set_mode((500, 500))
box_one_x = box_one_y = None
midpoint_x = midpoint_y = None
target_x = target_y = None
g_True = False
draw_while_drugged = False
box_two_list = []
target_list = []  # not needed but wanted press g

speed = 60
clock = pygame.time.Clock()

def distance(x, y, x1, y1):
    distance_ = x - x1, y - y1
    return distance_

Overlap_Forgiveness = 14 - 13  # <-- the lower this number the more forgiving, if its equal to Size then you can't die, 14 is the size of the player and targets
WarningImg = pygame.image.load('Box_warning.png')

while True:
    if target_x is not None:  # go to the target
        if target_y is not None:
            # moves the thing
            dx, dy = (box_one_x - target_x, box_one_y - target_y)
            stepx, stepy = (dx / 2, dy / 2)
            box_one_x -= stepx
            box_one_y -= stepy
            # removes element dynamically
            if dx < Overlap_Forgiveness and dx > -Overlap_Forgiveness:
                if dy < Overlap_Forgiveness and dy > -Overlap_Forgiveness:
                    box, boy = int(box_one_x), int(box_one_y)
                    for i in box_two_list:
                        if i == [box, boy]:
                            box_two_list.remove([box, boy])

    if box_one_x is not None:
        # draws the thing
        pygame.draw.rect(win, (255, 255, 0), (box_one_x, box_one_y, 14, 14))

    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        if event.type == pygame.MOUSEBUTTONDOWN:
            box_one_x, box_one_y = pos[0], pos[1]
            draw_while_drugged = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                box_two_list.append([pos[0], pos[1]])
                draw_while_drugged = True
            if event.key == pygame.K_g:
                g_True = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_g:
                g_True = False
        # f to create the targets, click to create the thing, g to see the path


    if len(box_two_list) > 0:
        if box_one_x is not None:
            if box_one_y is not None:
                n = 0
                n1 = 0

                # find target
                dis_list = []
                for _ in range(len(box_two_list)):
                    dis = [box_two_list[n1][0] - box_one_x, box_two_list[n1][1] - box_one_y]
                    # get distance from both x and y
                    # go through box two list and pick the one closest by making a algorithm to check both distances
                    # keep a "score" of the best one
                    # and if 1 then go to that one
                    dis_x, dis_y = abs(dis[0]), abs(dis[1])
                    dis_list.append([dis_x + dis_y, n1])
                    dis_list.sort()
                    if len(dis_list) == len(box_two_list):
                        target_x, target_y = box_two_list[dis_list[0][1]][0], box_two_list[dis_list[0][1]][1]
                        target_list.insert(0, [target_x, target_y])
                    n1 += 1

                # draw the boxes if click
                for _ in range(len(box_two_list)):
                    pygame.draw.rect(win, (255, 0, 255), (box_two_list[n][0], box_two_list[n][1], 14, 14))
                    n += 1

    # draw the red target line
    if g_True:
        if len(box_two_list) == 0:
            win.blit(WarningImg, (0, 0))
        if target_x is not None:
            pygame.draw.line(win, (255, 0, 0), (box_one_x, box_one_y), (target_list[1][0], target_list[1][1]))

    if draw_while_drugged:
        n2 = 0
        for _ in range(len(box_two_list)):
            pygame.draw.rect(win, (250, 0, 250), (box_two_list[n2][0], box_two_list[n2][1], 14, 14))
            n2 += 1
    # ending stuff
    pygame.display.update()
    clock.tick(speed)
    win.fill((0, 0, 0))
