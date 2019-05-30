from flask import Flask, render_template, request
import requests

app = Flask("MyApp")

@app.route('/')
def home():
    return render_template('quiz.html')

@app.route("/results", methods=['POST'])
def result():
    #creating a class to make it possible to tie how many times a bar got selected
#with its name
    class Bar:
        def __init__(self,name):
            self.name = name
            self.num = 0

    #return "final_result"



#creating instances for every bar option
    cahoots = Bar('Cahoots')
    bathouse = Bar('Bathouse')
    candlelight= Bar ('Candlelight')
    opium = Bar('Opium')

#getting the answers from the form and putting them in an array
    answers =[]
    q1 = request.form['q1']
    q2 = request.form['q2']
    q3 = request.form['q3']
    q4 = request.form['q4']
    q5 = request.form['q5']

    answers.append(q1)
    answers.append(q2)
    answers.append(q3)
    answers.append(q4)
    answers.append(q4)


#going through the form answers and seeing how many times each bar got selected
    for a in answers:
        if a == 'cahoots':
            cahoots.num += 1
        elif a == 'bathouse':
            bathouse.num +=1
        elif a == 'candlelight':
            candlelight.num += 1
        elif a == 'opium':
            opium.num += 1

#puts all the bars and their respective answer count in a list
    list =[]
    list.append(cahoots)
    list.append(bathouse)
    list.append(candlelight)
    list.append(opium)

#looks through each element in the list and assigns the name of the bar
# mentioned the most times to final_answer
    max_answer = 0
    final_answer =""
    for bar in list:
        if max_answer < bar.num:
            max_answer = bar.num
            final_answer = bar.name
            print final_answer
    print max_answer
    print "the answer is " + final_answer

# redirects the user to the corresponding result page

    if final_answer == "cahoots":
        return render_template("cahoots.html")
        #return ('Visit Cahoots: https://jazzy9.github.io/underground/cahoots.html')
    elif final_answer == "bathouse":
        return render_template("bathouse.html")
        #return ('Visit Bathouse: https://jazzy9.github.io/underground/bathouse.html')
    elif final_answer == "candlelight":
        return render_template("candlelight.html")
        #return ('Visit Candelight Club: https://jazzy9.github.io/underground/candelight.html')
    elif final_answer == "opium":
        return render_template("opium.html")
        #return ('Visit Opium: https://jazzy9.github.io/underground/candelight.html')

app.run(debug=True)
