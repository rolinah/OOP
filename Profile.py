# profile.py

class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact

    def introduce(self):
        print(f"Hi, I’m {self.name}. I love {self.favorite_language} and my hobby is {self.hobby}. Fun fact about me: {self.fun_fact}")

    def show_stack(self):
        print("Here is my tech stack:")
        for tool in self.tech_stack:
            print(f"- {tool}")

    def github_link(self):
        return f"https://github.com/{self.github_username}"


my_profile = Profile(
    name="Rolinah Asiimwe",
    favorite_language="Python",
    hobby="Reading novels",
    tech_stack=["Python", "Javascript", "HTML", "React"],
    github_username="rolinah",
    fun_fact="I can read novels the whole day!"
)


my_profile.introduce()
my_profile.show_stack()
print("GitHub link:", my_profile.github_link())
