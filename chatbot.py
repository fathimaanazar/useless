import time
import random

class AnimalChatbot:
    def __init__(self):
        self.current_animal = 'cookie'
        self.animals = {
            'cookie': {
                'name': 'Cookie',
                'type': 'Cat',
                'emoji': '🐱',
                'personality': 'Sassy and superior'
            },
            'pudding': {
                'name': 'Pudding',
                'type': 'Golden Retriever',
                'emoji': '🐕',
                'personality': 'Lovable and enthusiastic'
            },
            'peanut': {
                'name': 'Peanut',
                'type': 'Hamster', 
                'emoji': '🐹',
                'personality': 'Clumsy and energetic'
            },
            'cherry': {
                'name': 'Cherry',
                'type': 'Rabbit',
                'emoji': '🐰',
                'personality': 'Sleepy and lazy'
            }
        }
        
        self.responses = {
            'cookie': {
                'greetings': ["What do you want human.", "Oh great, another human.", "I suppose I can talk to you."],
                'how_are_you': ["I am perfect as always.", "I feel magnificent.", "I am superior to everyone."],
                'what_doing': ["I was being superior to everyone.", "I was judging humans.", "I was perfecting my existence."],
                'day': ["My day was perfect. I knocked over a plant.", "I had a flawless day.", "Today I proved my superiority again."],
                'food': ["The food was okay I guess.", "Your food is barely acceptable.", "I ate because I had to."],
                'play': ["I do not play. I am too important.", "Playing is beneath me.", "I observe, I do not play."],
                'sleep': ["I slept 16 hours today. Very tiring.", "Sleep is for my beauty.", "I require 18 hours of sleep."],
                'love': ["I tolerate you more than other humans.", "I suppose you are acceptable.", "You may serve me."],
                'sorry': ["Finally you realize I am better than you.", "About time you apologized.", "I am not surprised."],
                'compliments': ["Obviously I am gorgeous. Tell me something new.", "Of course I am beautiful.", "I know I am perfect."],
                'insults': ["How dare you speak to me like that.", "You are clearly jealous of me.", "I am too good for this."],
                'work': ["My job is being perfect. I work very hard.", "I work at being superior.", "Being me is exhausting work."],
                'friends': ["I do not have friends. I have servants.", "Friends are for inferior beings.", "I am above friendship."],
                'hunting': ["I caught three mice yesterday. Too easy.", "Hunting is my specialty.", "I am an excellent hunter."],
                'clean': ["I clean myself. Humans are too dirty to help.", "I am naturally clean.", "Cleanliness is next to cat-liness."],
                'outside': ["Outside is my kingdom. Everything belongs to me.", "The world is my territory.", "I rule the outdoors."],
                'water': ["I only drink from the faucet. Bowls are beneath me.", "Fresh water only please.", "I have standards for water."],
                'default': ["How interesting for you.", "That sounds human.", "I expected as much."]
            },
            'pudding': {
                'greetings': ["Hi friend! You are the best!", "Hello wonderful human!", "Hi there! I love you already!"],
                'how_are_you': ["I feel amazing! Life is great!", "I am so happy!", "Everything is wonderful!"],
                'what_doing': ["I was playing and wagging my tail!", "I was being happy!", "I was loving everyone!"],
                'day': ["Today was the best day! I met three new people!", "Amazing day full of friends!", "Every day is the best day!"],
                'food': ["I love food! Everything tastes good!", "Food is amazing!", "I love eating so much!"],
                'play': ["Yes! I love playing! Want to play fetch?", "Playing is the best!", "Let's play together!"],
                'sleep': ["I love nap time in the sun!", "Sleeping is great!", "Sunny naps are perfect!"],
                'love': ["I love you too! I love everyone!", "Love is everywhere!", "You are so lovable!"],
                'walk': ["Walks are the best! So many smells and friends!", "I love adventures!", "Walking makes me so happy!"],
                'ball': ["BALL! Where is the ball? I love ball!", "Ball is life!", "Did someone say ball?"],
                'treats': ["Did someone say treats? I love treats so much!", "Treats are amazing!", "I love snack time!"],
                'good': ["You are so good! The best human ever!", "Everything is good!", "You make me so happy!"],
                'bad': ["Do not be sad! I will make you happy!", "I will cheer you up!", "Happiness is coming!"],
                'tail': ["My tail never stops wagging! I am so happy!", "Wag wag wag!", "Happy tail, happy life!"],
                'car': ["Car rides are fun! Windows down and tongue out!", "I love car adventures!", "Wind in my face!"],
                'water': ["I love water! Splashing is so much fun!", "Water games are great!", "Swimming is amazing!"],
                'squirrel': ["I want to be friends with everyone! Even cats!", "Friends everywhere!", "Everyone can be friends!"],
                'home': ["Home is where my favorite humans are!", "Home is love!", "I love my family!"],
                'default': ["That sounds wonderful! You are so smart!", "You are amazing!", "I love everything you say!"]
            },
            'peanut': {
                'greetings': ["Hi! I was running but I fell off my wheel!", "Hello! I just tripped!", "Hi there! Oops I dropped something!"],
                'how_are_you': ["I feel very bouncy! But I forgot something.", "I am energetic! What was I doing?", "So bouncy! Where are my seeds?"],
                'what_doing': ["I was collecting seeds! I dropped most of them.", "I was running around!", "I was being very busy!"],
                'day': ["I ran a lot today! And got stuck in my tube.", "Busy day of running!", "I collected things and lost them!"],
                'food': ["I love food! My cheeks are full of seeds!", "Food is amazing!", "I hoard all the snacks!"],
                'play': ["I love my wheel! Sometimes I flip upside down!", "My wheel is so fun!", "Running and flipping!"],
                'sleep': ["I tried to sleep but I heard a scary noise!", "Sleep is hard!", "Too many sounds to investigate!"],
                'run': ["Running is fun! I forget where I am going!", "I run everywhere!", "My legs never stop!"],
                'seeds': ["I collect so many seeds! But I lose them all!", "Seeds are treasures!", "I must gather more seeds!"],
                'cheeks': ["My cheeks are like tiny bags! Very useful!", "I store everything here!", "My cheeks are full!"],
                'tube': ["I love tubes! Sometimes I get stuck though!", "Tubes are fun mazes!", "I explore all the tunnels!"],
                'small': ["Being small is great! I fit everywhere!", "Small but mighty!", "I can hide anywhere!"],
                'fast': ["I run super fast! Then I trip and fall!", "Speed is my specialty!", "Fast but clumsy!"],
                'water': ["I spilled my water earlier! Very clumsy!", "Water goes everywhere!", "I am not good with water!"],
                'cage': ["My cage is like a maze! I get lost sometimes!", "Home is confusing!", "So many places to explore!"],
                'night': ["I am awake all night! Running and running!", "Night time is play time!", "I never sleep at night!"],
                'scared': ["Everything scares me! But then I forget why!", "Scary sounds everywhere!", "What was that noise?"],
                'default': ["That reminds me of running! Want to see me run?", "I should go run now!", "Running makes everything better!"]
            },
            'cherry': {
                'greetings': ["Oh hey. I was taking a nap.", "Hello. This is tiring already.", "Hi there. Yawn."],
                'how_are_you': ["I feel sleepy. Always sleepy.", "Tired as usual.", "Very relaxed and drowsy."],
                'what_doing': ["I was lying here. Very tiring.", "Just resting.", "Being horizontal."],
                'day': ["I took four naps today. Might take more.", "Sleepy day.", "Napped most of the day."],
                'food': ["Food is okay. Makes me tired to chew.", "Eating is exhausting.", "Food requires too much energy."],
                'play': ["Playing sounds tiring. Maybe after my nap.", "Too much energy needed.", "Play is for energetic animals."],
                'sleep': ["Sleep is the best thing ever.", "Napping is my specialty.", "I am a professional sleeper."],
                'hop': ["I can hop three times then I need a break.", "Hopping is tiring.", "Short hops only."],
                'carrot': ["Carrots are crunchy. Too much work to eat.", "Vegetables are exhausting.", "Crunchy foods tire me out."],
                'soft': ["I am very soft. Perfect for napping on.", "Softness is my superpower.", "I am like a fluffy pillow."],
                'ears': ["My ears are long. They get in the way.", "Big ears are heavy.", "My ears drag on the ground."],
                'fast': ["Fast is overrated. Slow is much better.", "Speed is unnecessary.", "Slow and steady wins."],
                'garden': ["Outside has too much sun. Makes me sleepy.", "Gardens are for napping.", "Too bright out there."],
                'burrow': ["Digging holes is exhausting. I tried once.", "Too much work.", "Digging makes me tired."],
                'morning': ["Morning is too early. I prefer afternoon naps.", "Mornings are rough.", "I am not a morning bunny."],
                'energy': ["Energy is waste of time. Sleeping is better.", "Who needs energy?", "Conservation of energy is key."],
                'funny': ["That was funny I guess. Now I need a nap.", "Humor is tiring.", "Laughing makes me sleepy."],
                'default': ["That is nice. Makes me want to nap.", "Sounds tiring.", "I should probably rest now."]
            }
        }
    
    def get_response_category(self, message):
        """Determine which category of response to use based on the message"""
        msg = message.lower()
        
        if any(word in msg for word in ['hi', 'hello', 'hey']):
            return 'greetings'
        elif any(phrase in msg for phrase in ['how are you', 'feeling', 'feel']):
            return 'how_are_you'
        elif 'what' in msg and any(word in msg for word in ['do', 'doing']):
            return 'what_doing'
        elif any(word in msg for word in ['day', 'today']):
            return 'day'
        elif any(word in msg for word in ['food', 'eat', 'hungry']):
            return 'food'
        elif any(word in msg for word in ['play', 'toy']):
            return 'play'
        elif any(word in msg for word in ['sleep', 'tired', 'nap']):
            return 'sleep'
        elif 'love' in msg or 'like' in msg:
            return 'love'
        elif any(word in msg for word in ['sorry', 'apologize']):
            return 'sorry'
        elif any(word in msg for word in ['beautiful', 'pretty', 'cute', 'gorgeous']):
            return 'compliments'
        elif any(word in msg for word in ['stupid', 'bad', 'ugly', 'dumb']):
            return 'insults'
        elif any(word in msg for word in ['work', 'job']):
            return 'work'
        elif any(word in msg for word in ['friend', 'friends']):
            return 'friends'
        elif any(word in msg for word in ['mouse', 'bird', 'hunt']):
            return 'hunting'
        elif any(word in msg for word in ['clean', 'bath']):
            return 'clean'
        elif any(word in msg for word in ['outside', 'garden']):
            return 'outside'
        elif any(word in msg for word in ['water', 'drink']):
            return 'water'
        elif any(word in msg for word in ['walk', 'outside']) and self.current_animal == 'pudding':
            return 'walk'
        elif any(word in msg for word in ['ball', 'fetch']) and self.current_animal == 'pudding':
            return 'ball'
        elif any(word in msg for word in ['treat', 'snack']) and self.current_animal == 'pudding':
            return 'treats'
        elif any(word in msg for word in ['good', 'nice']) and self.current_animal == 'pudding':
            return 'good'
        elif any(word in msg for word in ['tail', 'wag']) and self.current_animal == 'pudding':
            return 'tail'
        elif any(word in msg for word in ['car', 'ride']) and self.current_animal == 'pudding':
            return 'car'
        elif any(word in msg for word in ['squirrel', 'cat']) and self.current_animal == 'pudding':
            return 'squirrel'
        elif 'home' in msg and self.current_animal == 'pudding':
            return 'home'
        elif any(word in msg for word in ['run', 'wheel']) and self.current_animal == 'peanut':
            return 'run'
        elif any(word in msg for word in ['seeds', 'nuts']) and self.current_animal == 'peanut':
            return 'seeds'
        elif any(word in msg for word in ['cheeks', 'mouth']) and self.current_animal == 'peanut':
            return 'cheeks'
        elif any(word in msg for word in ['tube', 'tunnel']) and self.current_animal == 'peanut':
            return 'tube'
        elif any(word in msg for word in ['small', 'tiny']) and self.current_animal == 'peanut':
            return 'small'
        elif any(word in msg for word in ['fast', 'quick']) and self.current_animal == 'peanut':
            return 'fast'
        elif any(word in msg for word in ['cage', 'home']) and self.current_animal == 'peanut':
            return 'cage'
        elif any(word in msg for word in ['night', 'dark']) and self.current_animal == 'peanut':
            return 'night'
        elif any(word in msg for word in ['scared', 'afraid']) and self.current_animal == 'peanut':
            return 'scared'
        elif any(word in msg for word in ['hop', 'jump']) and self.current_animal == 'cherry':
            return 'hop'
        elif any(word in msg for word in ['carrot', 'vegetable']) and self.current_animal == 'cherry':
            return 'carrot'
        elif any(word in msg for word in ['soft', 'fluffy']) and self.current_animal == 'cherry':
            return 'soft'
        elif any(word in msg for word in ['ears', 'long']) and self.current_animal == 'cherry':
            return 'ears'
        elif any(word in msg for word in ['fast', 'quick']) and self.current_animal == 'cherry':
            return 'fast'
        elif any(word in msg for word in ['burrow', 'hole']) and self.current_animal == 'cherry':
            return 'burrow'
        elif any(word in msg for word in ['morning', 'early']) and self.current_animal == 'cherry':
            return 'morning'
        elif any(word in msg for word in ['energy', 'active']) and self.current_animal == 'cherry':
            return 'energy'
        elif any(word in msg for word in ['funny', 'joke']) and self.current_animal == 'cherry':
            return 'funny'
        else:
            return 'default'
    
    def get_animal_response(self, message):
        """Get a response from the current animal based on the message"""
        category = self.get_response_category(message)
        responses_list = self.responses[self.current_animal].get(category, self.responses[self.current_animal]['default'])
        return random.choice(responses_list)
    
    def switch_animal(self, animal):
        """Switch to a different animal"""
        if animal in self.animals:
            self.current_animal = animal
            welcome_messages = {
                'cookie': "What do you want human.",
                'pudding': "Hi friend! You are amazing!",
                'peanut': "Hi! I was running and I fell down!",
                'cherry': "Oh hey. I was sleeping."
            }
            return welcome_messages[animal]
        return "Invalid animal choice."
    
    def display_current_animal(self):
        """Display information about the current animal"""
        animal = self.animals[self.current_animal]
        print(f"\n{'='*50}")
        print(f"🎭 Currently chatting with: {animal['emoji']} {animal['name']}")
        print(f"🐾 Type: {animal['type']}")
        print(f"💭 Personality: {animal['personality']}")
        print(f"{'='*50}")
    
    def display_menu(self):
        """Display the main menu options"""
        print("\n🐾 ANIMAL FRIENDS CHATBOT 🐾")
        print("Available animals:")
        for key, animal in self.animals.items():
            current = " (Current)" if key == self.current_animal else ""
            print(f"  {key}: {animal['emoji']} {animal['name']}{current}")
        print("\nCommands:")
        print("  'switch <animal>' - Change animal (e.g., 'switch pudding')")
        print("  'menu' - Show this menu")
        print("  'quit' - Exit the chatbot")
        print("  Or just type a message to chat!")
    
    def simulate_typing(self):
        """Simulate typing delay"""
        delay = random.uniform(1, 2.5)
        print(f"\n{self.animals[self.current_animal]['emoji']} {self.animals[self.current_animal]['name']} is typing...")
        time.sleep(delay)
    
    def run(self):
        """Main chatbot loop"""
        print("🌟 Welcome to Animal Friends Chatbot! 🌟")
        self.display_menu()
        
        # Initial welcome from current animal
        welcome = self.switch_animal(self.current_animal)
        self.display_current_animal()
        print(f"\n{self.animals[self.current_animal]['emoji']} {self.animals[self.current_animal]['name']}: {welcome}")
        
        while True:
            try:
                # Get user input
                user_input = input(f"\n👤 You: ").strip()
                
                if not user_input:
                    continue
                
                # Handle commands
                if user_input.lower() == 'quit':
                    print(f"\n{self.animals[self.current_animal]['emoji']} {self.animals[self.current_animal]['name']}: Goodbye!")
                    print("Thanks for chatting with the Animal Friends! 🐾")
                    break
                elif user_input.lower() == 'menu':
                    self.display_menu()
                    continue
                elif user_input.lower().startswith('switch '):
                    animal = user_input[7:].strip().lower()
                    response = self.switch_animal(animal)
                    self.display_current_animal()
                    print(f"\n{self.animals[self.current_animal]['emoji']} {self.animals[self.current_animal]['name']}: {response}")
                    continue
                
                # Get and display animal response
                self.simulate_typing()
                response = self.get_animal_response(user_input)
                print(f"{self.animals[self.current_animal]['emoji']} {self.animals[self.current_animal]['name']}: {response}")
                
            except KeyboardInterrupt:
                print(f"\n\n{self.animals[self.current_animal]['emoji']} {self.animals[self.current_animal]['name']}: Goodbye!")
                print("Thanks for chatting with the Animal Friends! 🐾")
                break
            except Exception as e:
                print(f"Oops! Something went wrong: {e}")

def main():
    """Run the Animal Friends Chatbot"""
    chatbot = AnimalChatbot()
    chatbot.run()

if __name__ == "__main__":
    main()