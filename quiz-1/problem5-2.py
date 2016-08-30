import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    sameCount = 0
    for i in range(numTrials):
        balls = ["g1", "g2", "g3", "g4", "r1", "r2", "r3", "r4"]
        choices = []
        for i in range(3):
            choice = random.choice(balls)
            balls.remove(choice)
            choices.append(choice)
        colors = map(lambda x: x[0], choices)
        if len(set(colors)) == 1:
            sameCount += 1
    return float(sameCount)/float(numTrials)

print drawing_without_replacement_sim(1000)
