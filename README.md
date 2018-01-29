
# Back-end interview exercise
A short exercise to work on, as a technical interview preparation


## Instructions
In this project, you will find a server application built with Python and Django and some others Python modules.
The app is a small autonomous chat api service, aimed to serve several client applications of different types (web, mobile, connected devices).

Unfortunately, this application is not finished, and some parts are broken 🤕 !

Your mission, if you accept it 😎, will be to finish what's missing and make it works.

- First, you have to get ready for development. **Fork the project on github, get the files on your computer, setup the environment, then start the development server**. If you open a browser at [localhost:8000](http://localhost:8000/), you should be able to access the browsable api, so you can test the app easily. You can also check out the [generated api documentation](http://localhost:8000/docs/) where you can test each endpoint too.
- The *Conversation* api resource is not fully finished. The 'create' endpoint sends a response, but do nothing internally right now. **Add some logic to the ConversationViewSet class** so it adds a row in the database.
- It seems there is a bug with the *Message* resource : the api endpoint respond with a 500 - internal server error. **Find the source of that bug, and solve it** to make it work.
- Nice ! Now, we want to add a new feature to the message creation endpoint. Right now, a profile earn 1 point each time he post a new message to a conversation. Let's say we want to create an automatic congratulation message every time a profile reaches a multiple of 10 points for his total (10, 20, 30, etc). The congratulation message should be added to the same conversation of the message that triggered it, and it should have an empty author. There is already an *instantiate_reward_message* function in *api/utils.py* file that prepare the automatic message, but you would have to **write the logic to call it appropriately**. How would you do that ? Implement the changes in the *MessageSerializer* class.
- Great job ! The application is ready. **Commit and push the changes to your Github repo** and when you're ready, **[create a pull request](https://help.github.com/articles/creating-a-pull-request/) on the origin repository on Github** so we can review your work before the meeting.


## Project setup
This project uses [Django framework](https://www.djangoproject.com/) and so, it follows its structure.

First, make sure you have *Python 3*, *pip* and *virtualenv* installed on your computer.
If that's not the case, check out [that guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

Then, install project dependencies:
```shell
# create a virtual env for the project
virtualenv -p python3 venv

# Activate it
source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt
```

Run the server using django tools:
```shell
python manage.py runserver
```


## Rules to remember
- It should take between 1 to 3 hour(s) to complete it, depending on your approach and your knowledge (maybe some more if you never used Django before). Try not to make it bigger than what it is.
- Don't sweat it. If you're stuck, take notes of what you have so we can talk about it during the meeting and see how to solve it.
- Commenting your code to explain what you've done is always welcome.
