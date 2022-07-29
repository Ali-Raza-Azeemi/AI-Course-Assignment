print('******Marksheet********')

Math = int(input('Enter marks Math = '))
Physics = int(input('Enter marks Physics = '))
Chemistry = int(input('Enter marks Chemistry = '))
English = int(input('Enter marks English = '))
Urdu = int(input('Enter marks Urdu = '))
total_obtained_marks = Math + Physics + Chemistry + English + Urdu
percentage = total_obtained_marks / 500 * 100
if percentage >= 90:
    print(percentage, 'Congratulations! You have secur1ed A-1')
elif percentage >= 80:
    print(percentage, 'You have secured A')
elif percentage >= 70:
    print(percentage, 'You have secured B')

