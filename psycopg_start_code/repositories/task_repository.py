from db.run_sql import run_sql
from models.task import Task
from models.user import User
import user_repository

def select_all():
# create a SQL statement
    tasks = []
    sql = "SELECT * FROM tasks"
# execute SQL statement
# Get Results
    results = run_sql(sql)
    
    for row in results:
        user = user_repository.select(row['user_id'])
        task = Task( 
            row["description"], 
            row["assignee"], 
            row["duration"],
            row["completed"],
            row["id"]
            )
        tasks.append(task)

# I want to get a list of Task objects
    return tasks

# Create 
# def save(task):
#     sql = f"INSERT INTO tasks (description, assignee, duration, completed) VALUES (%s, %s, %s ,%s) RETURNING *"
#     values = [task.description, task.assignee, task.duration, task.completed]
#     run_sql(sql, values)
# # as Values expected are('{task.description}', '{task_assignee}', {task.duration}, {task.completed})"
# # %s acts as place holder and substitutes above values 
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     task.id = id
#     return task



def save(task):
    sql = "INSERT INTO tasks (description, user_id, duration, completed) VALUES (%s, %s, %s, %s) RETURNING *" # MODIFIED
    values = [task.description, task.user.id, task.duration, task.completed] 
    results = run_sql(sql, values)
    id = results[0]['id']
    task.id = id
    return task


def select(id):
    task = None
    sql = "SELECT * FROM tasks WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        task = Task(result['description'], result['assignee'], result['duration'], result['completed'], result['id'])
        
    return task

# DELETE ALL
def delete_all():
    sql = "DELETE FROM tasks"
    run_sql(sql)
    
# DELETE ONE
def delete_one(id):
    sql = "DELETE FROM tasks WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
# UPDATE
def update(task):
    sql = "UPDATE tasks SET (description, assignee, duration, completed) = (%s, %s, %s, %s) WHERE id = %s"
    values = [task.description, task.assignee, task.duration, task.completed, task.id]
    run_sql(sql, values)
    
    