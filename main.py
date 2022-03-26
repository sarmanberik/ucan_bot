import telebot
from google_connection import get_value


token = '5274414928:AAGJRyWit56t6pjLRTPcfFeJWV0FIWuaxMw'

bot = telebot.TeleBot(token)
students = ['Жолдасбек Әділет 6КОУ', 'Мәлік Алуа 6КОУ', 'Қыдырәлі Балауса 6КОУ', 'Серікбай Қарақат  6КОУ', 'Амангелді '
                                                                                                           'Таңшолпан '
                                                                                                           '6КОУ',
            'Абдрахман Шынар 6КОУ', 'Әмзе Айкен 6 КОУ', 'Сейдулла Серік 6КОУ', 'Әбдиева Шұғыла 6КОУ',
            'Дайрабай Жанәділ 6коу', 'Прмат Аружан 6КОУ', 'Райымбек Талшын 6КОУ', 'Мырзатай Арайлым 6КОУ',
            'Әбдіразақ Ақбаян 6КОУ', 'Есжан Нариман 6КОУ', 'Абдумуталиев Жасур 6КОУ', 'Асыланұлы Ернұр 6 КОУ',
            'Маулен Нурислам 6КОУ', 'Әділхан Абдеш  6 КОУ', 'Набиева Асель 6 КОУ', 'Абибулла Рауана  6КОУ',
            'Исмаилов Ерболат 6КОУ', 'Құлбек АҚЖАРҚЫН 6КОУ', 'Құлбек Ақмаржан  6КОУ', 'Адилов Мадияр 6КОУ',
            'Кемелбек Дария 6КОУ', 'Мухумов Өтеген 6КОУ', 'Құлбек Әділбек  6КОУ', 'Амалбек Алмасбек 6 КОУ',
            'Әділ Камалия 6 КОУ', 'Қалыбек Жандос 6 КОУ', 'Толепбай Айзере 6 КОУ', 'Рахметова Томирис 5КОВ',
            'Оразалы Дарын 4 КОВ', 'Сауырбай Алихан 4КОВ', 'Ержігіт Көркем 4КОВ', 'Назарұлы Ғазиз 4 КОВ',
            'Серікбай Нұрбек 4 КОВ', 'Жаңабай Әлжан 6 КОВ', 'Ілесбай Нұрахмет 6 КОВ', 'Төлебай Нұрбақ 6КОВ',
            'Қалдан Саян 6КОВ', 'Сұлтанмұрат Арайлым 6 КОВ', 'Ибрахим Бауыржан  6 КОУ', 'Амангелді Луара 6КОУ',
            'Дүйсенбек Жәния 6КОУ', 'Ахмет Мирас 6КОУ', 'Надирова Надира 5КОУ', 'Мырзахмет Аяла 5 КОУ', 'Жолдашева '
                                                                                                        'Жанылай '
                                                                                                        '5КОУ',
            'Бабайхан Нұрали 5КОУ', 'Исабек Муслим 5КОВ', 'Берік Нурислам 5КОУ', 'Нұрмұхаммед Көркем 5КОУ',
            'Мусабекова Аиша 4КОУ', 'Бақытжан Асылжан 4КОУ', 'Әшірәлі Мағжан 5 КОУ', 'Сәрсен Ерасыл 5 КОУ',
            'Хаумет Димаш 4КОУ', 'Алшынбай Алинұр  5 КОУ', 'Ағабек Мирас  4КОУ', 'Камилханов Иброхим  5КОУ',
            'Мизанбай Дарын  4КОУ', 'Оспан Таңат 5КОУ', 'Хайрулла Іңкәр 5КОУ', 'Курбаналиева Фарзона 6 КОУ',
            'Абылғазы Інжу 6КОУ', 'Мамиржанова Севинч 6КОУ', 'Бекназаров Алибек 6КОУ', 'Ермахан Асылай 5КОВ',
            'Ғабит Бекасыл 6КОВ', 'Ермахан Ұлсана 6КОВ', 'Нұрболқызы  Ұлдария  4КОУ', 'Әлмахамбет Таңнұр 4КОУ',
            'Дайрабай Анел 4 КОВ', 'Дайрабай Жанел 4 КОВ']


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    text = 'Student not found'

    if message.text in students:
        arr = get_value(message.text)
        print(arr)
        for each in arr:
            text = "ФИО ТРЕНЕРА: {}\n" \
                   "ФИО УЧЕНИКА: {}\n" \
                   "ПРЕДМЕТ: {}\n" \
                   "{}\n" \
                   "{}\n" \
                   "{}\n" \
                   "КОММЕНТАРИИ: {}\n" \
                   "ДАТА: {}\n".format(each[1], each[2], each[3], each[4], each[5], each[6], each[8], each[0])
            bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, text)


if __name__ == '__main__':
    bot.infinity_polling()
