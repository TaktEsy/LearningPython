import hashlib
class UrTube():

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        for user in self.users:
            if user['nickname'] == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        new_user = {
            'nickname': nickname,
            'password': password,
            'age': age
        }
        self.users.append(new_user)

        # автоматический вход после регистрации
        self.log_in(nickname, password)

    def log_in(self, nickname, password):
        for user in self.users:
            if user['nickname'] == nickname and user['password'] == password:
                self.current_user = user
                print('Successfully logged in as', nickname)

        return print('Invalid nickname or password')

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        search_word = search_word.lower()
        result = []

        for video in self.videos:

            if search_word in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, video_title):

        for video in self.videos:

            if video_title in video.title:
                print(f"Воспроизводится видео: {video.title}")
            else:
                print("Видео не найдено!")
                # if video_title in video:
                #
                #     for second in range(1, 11):
                #         time.sleep(1)
                #         print(f"Секунда воспроизведения: {second}")
                #     print("Конец видео")
                #
                #     return
                #     print("Видео не найдено")

class User(UrTube):
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.__hash__(password)
        self.age = age

        def _hash_password(self, password):
            # Хэшируем пароль с помощью SHA-256
            return int(hashlib.sha256(password.encode()).hexdigest(), 16)

class Video(UrTube):

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

print("===============================")
print("Добавление видео: ")
ur.add(v1, v2)

print("===============================")
print("Поиск: ")
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

print("===============================")
print("Вход и возрастное ограничение")
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

print("===============================")
print("Вход в другой аккаунт: ")
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)


print("===============================")
print("Попытка воспроизведения несуществующего видео: ")
ur.watch_video('Лучший язык программирования 2024 года!')





