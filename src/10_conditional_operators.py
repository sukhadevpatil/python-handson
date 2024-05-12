your_score = 89
passing_score = 50
credit_score = 70
distinction_score = 90

if your_score >= passing_score:
    print('Congrats!!!')
    print('You have passed the exam.')
else:
    print('You did not pass the exam')
    print('Please try again after 15 days.')

print('Thank you taking the exam...')
print('================================================')

if your_score >= distinction_score:
    print('Congrats!')
    print('You have passed with DISTINCTION!')
elif your_score >= credit_score:
    print('Congrats!')
    print('You have passed with CREDIT!')
    if your_score >= distinction_score-5:
        print(f'You missed distinction by score {distinction_score - your_score}')
elif your_score >= passing_score:
    print('Congrats!')
    print('You have passed!')
else:
    print('You did not pass the exam')

print('Thank you for taking the exam.')
