kotowaza = ["1. A drowning man will clutch at a straw.",
"2. A journey of a thousand miles begins with a single step.",
"3. A bad workman always blames his tools.",
"4. A bird in the hand is worth two in the bush",
"5. All's well that ends well",
"6. A picture is worth a thousand words.",
"7. A rolling stone gathers no moss.",
"8. A barking dog seldom bites.",
"9. Don't judge a book by its cover",
"10. Kill two birds with one stone",
"11. Like father, like son",
"12. It's no use crying over spilled milk",
"13. Rome wasn't built in a day",
"14. God helps those who help themselves",
"15. You can't make an omelette without breaking eggs.",
"16. An apple a day keeps the doctor away.",
"17. No pain, no gain.",
"18. Look before you leap.",
"19. Too many cooks spoil the broth.",
"20. Make hay while the sun shines.",
"21. Many drops make a shower.",
"22. Two heads are better than one.",
"23. Let sleeping dogs lie.",
"24. Better to be the head of a dog, than the tail of a lion.",
"25. Never look a gift horse in the mouth.",
"26. A watched pot never boils.",
"27. Don't bite the hand that feeds you.",
"28. One man's trash is another man's treasure.",
"29. There's no time like the present.",
"30. A broken clock is right twice a day.",
"31. A lie travels around the world while truth is putting her boots on.",
"32. If you dig a hole for someone else, you'll fall into it.",
"33. Anger can be an expensive luxury.",
"34. Out of the frying pan and into the fire.",
"35. A closed mouth catches no flies.",
"36. The woman cries before the wedding, the man after."]

def returnSaying(num):
    return kotowaza[num-1]

def returnLength():
    return len(kotowaza)

print(returnLength())