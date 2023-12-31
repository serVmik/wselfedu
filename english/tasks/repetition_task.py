from random import choice, shuffle

from django.forms.models import model_to_dict

from english.models import WordUserKnowledgeRelation
from users.models import UserModel


def get_random_sequence_language_keys() -> list[str]:
    """Return a random sequence of language keys."""
    language_keys = ['words_eng', 'words_rus']
    shuffle(language_keys)
    return language_keys


def add_filers_to_queryset(request, words_qs, task_status):
    """Добавь фильтры в QuerySet."""
    # Получи словарь фильтров.
    words_filter = request.session.get('words_filter', dict())

    # Обнови словарь фильтров.
    assess = []
    if task_status == 'start':
        words_filter['category_id'] = request.GET.get('category_id')
        words_filter['source_id'] = request.GET.get('source_id')
        words_filter['word_count'] = (
            request.GET.get('word_count_ow'),
            request.GET.get('word_count_cb'),
            request.GET.get('word_count_ps'),
            request.GET.get('word_count_st'),
            'NC',
        )
        assess.extend([0, 1, 2, 3, 4, 5]) if request.GET.get('ws') else None
        assess.extend([6, 7, 8]) if request.GET.get('ck') else None
        assess.extend([9, 10]) if request.GET.get('ch') else None
        words_filter['assessment'] = assess

    # Добавь последовательно фильтры к QuerySet.
    category_id = words_filter.get('category_id')
    if category_id:
        words_qs = words_qs.filter(category_id=category_id)
    source_id = words_filter.get('source_id')
    if source_id:
        words_qs = words_qs.filter(source_id=source_id)
    words_qs = words_qs.filter(word_count__in=words_filter['word_count'])

    # Добавь фильтрацию по уровню знания слова.
    user = request.user
    word_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    assessment = set(words_filter['assessment'])
    if user.is_authenticated:
        words_id_for_choice = []
        if len(assessment) == 6:
            # Выбирает к показу слова, в том числе не имеющие оценку.
            not_showing_words_pk = WordUserKnowledgeRelation.objects.filter(
                user=UserModel.objects.get(pk=user.id),
            ).filter(
                knowledge_assessment__in=(word_set - assessment)
            ).values_list('word_id', flat=True)
            # Добавь фильтрацию.
            for word_obj in words_qs:
                if word_obj.pk not in not_showing_words_pk:
                    words_id_for_choice.append(word_obj)
        else:
            # Выбери к показу слова, только имеющие оценку.
            # Создай список id слов, только имеющих оценку.
            showing_words_pk = WordUserKnowledgeRelation.objects.filter(
                user=UserModel.objects.get(pk=user.id),
            ).filter(
                knowledge_assessment__in=assessment,
            ).values_list('word_id', flat=True)
            # Собери список слов, чей id есть в списке слов имеющих необходимую
            # оценку.
            for word_obj in words_qs:
                if word_obj.pk in showing_words_pk:
                    words_id_for_choice.append(word_obj)
        words: list = words_id_for_choice
    else:
        words: list = words_qs

    # Обнови словарь фильтров в сессии.
    if words_filter:
        request.session['words_filter'] = words_filter

    return words


def choice_word(words: list) -> dict:
    """Создай задание для изучения слов."""
    # Выбери случайным образом слово для перевода.
    selected_word = model_to_dict(choice(words))
    # Выбери случайным образом язык слова для перевода.
    question_key, answer_key = get_random_sequence_language_keys()
    # Сформируй словарь с условиями упражнения.
    word = {
        'word_id': selected_word.get('id'),
        'question': selected_word.get(question_key),
        'answer': selected_word.get(answer_key),
    }
    return word
