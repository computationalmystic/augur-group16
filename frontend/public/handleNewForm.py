import mysql.connector
from Flask import request, redirect
app = Flask(__name__)

mydb = mysql.connector.connect(
  host="rji.augurlabs.io",
  user="austin",
  passwd="texas2019",
  database="git_sixteen"
)
print("This should print")
@app.route('/handleNewForm', methods = ['POST'])
def handleNewForm():
    print("This should print")
    name = request.form['name']
    goal1 = request.form['goal1']
    goal2 = request.form['goal2']
    goal3 = request.form['goal3']
    url = request.form['url']
    description = request.form['projectDescription']
    
    mycursor = mydb.cursor()

    sql = "INSERT INTO  repo_info(repoName, url, goal1, goal2, goal3) VALUES (%s, %s, %s, %s, %s)"
    val = (name, goal1, goal2, goal3, url)
    mycursor.execute(sql, val)

    mydb.commit()
    
    print("The name is " +name)
    
    return redirect('/NewForm.vue')

if __name__ == "__main__":
    app.run()

# mycursor = mydb.cursor()
#
#sql = "INSERT INTO  repo_info(repoID, repoName, url, goal1, goal2, goal3, description) VALUES (%s, %s)"
#val = ("John", "Highway 21")
#mycursor.execute(sql, val)
#
#mydb.commit()
#
#print(mycursor.rowcount, "record inserted.")
