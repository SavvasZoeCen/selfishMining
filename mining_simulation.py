import random

#alpha: selfish miners mining power (percentage),
#gamma: the ratio of honest miners choose to mine on the selfish miners pool's block
#N: number of simulations run
def Simulate(alpha,gamma,N, seed):
    
    # DO NOT CHANGE. This is used to test your function despite randomness
    random.seed(seed)
  
    #the same as the state of the state machine in the slides 
    state=0
    # the length of the blockchain
    ChainLength=0
    # the revenue of the selfish mining pool
    SelfishRevenue=0
    # the length of hidden blocks
    HiddenBlocks=0

    print("alpha,gamma,N,seed:", alpha,gamma,N,seed)
    #A round begin when the state=0
    for i in range(N):
        #print(state)
        r=random.random()
        if state==0:
            #The selfish pool has 0 hidden block.
            if r<=alpha:
                #The selfish pool mines a block.
                #They don't publish it. 
                # ChainLength no change
                # HiddenBlocks=1
                state=1
            else:
                #The honest miners found a block.
                #The round is finished : the honest miners found 1 block
                # and the selfish miners found 0 block.
                ChainLength+=1
                # HiddenBlocks=0
                state=0

        elif state==1:
            #The selfish pool has 1 hidden block.
            if r<=alpha:
                #The selfish miners found a new block.
                #Write a piece of code to change the required variables.
                #You might need to define new variable to keep track of the number of hidden blocks.
                # ChainLength no change
                HiddenBlocks=2
                state=2
            else:
                #Write a piece of code to change the required variables.
                ChainLength+=1
                # (f) Lead was 1, others find a block.
                HiddenBlocks=0  #If the pool has a private branch of length 1 and the others mine one block, the pool publishes its branch, which results in two public branches of length 1
                state=-1

        elif state==-1:
            #It's the state 0' in the slides (the paper of Eyal and Gun Sirer)
            #There are three situations! 
            #Write a piece of code to change the required variables in each one.
            if r<=alpha:
                SelfishRevenue+=2
                ChainLength+=1
                # HiddenBlocks no change
                state=0
            elif r<=alpha+(1-alpha)*gamma:
                SelfishRevenue+=1
                ChainLength+=1
                # HiddenBlocks no change
                state=0
            else:
                # SelfishRevenue no change, Others obtain a revenue of two
                ChainLength+=1
                # HiddenBlocks no change
                state=0

        elif state==2:
            #The selfish pool has 2 hidden block.
            if r<=alpha:
                # ChainLength no change
                HiddenBlocks+=1
                state+=1
            else:
                #The honest miners found a block.
                ChainLength+=2
                SelfishRevenue+=2  # (g) Lead was 2, others find a block.
                HiddenBlocks=0  #If the others mine a block when the lead is two, the pool publishes its private branch, and the system drops to a lead of 0.
                state=0

        elif state>2:
            if r<=alpha:
                #The selfish miners found a new block
                # ChainLength no change
                HiddenBlocks+=1
                state+=1
            else:
                #The honest miners found a block
                ChainLength+=1   #?
                SelfishRevenue+=1  # (h) Lead was more than 2, others win.
                HiddenBlocks-=1  #?
                state-=1

    print("state,ChainLength,SelfishRevenue,HiddenBlocks:",state,ChainLength,SelfishRevenue,HiddenBlocks)
    return float(SelfishRevenue)/ChainLength


""" 
  Uncomment out the following lines to try out your code
  DON'T include it in your final submission though.
"""

"""
#let's run the code with the follwing parameters!
alpha=0.35
gamma=0.5
Nsimu=10**7
seed = 100
#This is the theoretical probability computed in the original paper
print("Theoretical probability :",(alpha*(1-alpha)**2*(4*alpha+gamma*(1-2*alpha))-alpha**3)/(1-alpha*(1+(2-alpha)*alpha)))
print("Simulated probability :",Simulate(alpha,gamma,Nsimu, seed))
"""
