#First we convert the index(which records the range that this tap can cover), now we have the range that each tap covers
#Since the leftmost point must be covered, we can ensure that there must be at least one tap will be opened to cover the leftmost 
#Among all the taps open, we choose the tap with rightmost range since this is the best choice.
#Now we update the leftmost range to the leftmost cell uncovered, with that we choose the one which cover the current leftmost which covers furtherest
