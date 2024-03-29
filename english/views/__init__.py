from english.views.account_views import (
    UserWordListView,
)
from english.views.home import (
    HomeEnglishView,
)
from english.views.crud_categories import (
    CategoryCreateView,
    CategoryListView,
    CategoryUpdateView,
    CategoryDeleteView,
    CategoryDetailView,
)
from english.views.crud_word import (
    WordCreateView,
    WordListView,
    WordDetailView,
    WordUpdateView,
    WordDeleteView,
)
from english.views.crud_sources import (
    SourceCreateView,
    SourceUpdateView,
    SourceDeleteView,
    SourceListView,
    SourceDetailView
)
from english.views.word_task_view import (
    AnswerWordStudyView,
    WordChoiceView,
    QuestionWordStudyView,
    start_study_word_view,
    update_words_favorites_status_view,
    update_words_knowledge_assessment_view,
)
