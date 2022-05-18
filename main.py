from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill


def main():
    app = Flask(__name__)

    # Создание списка кандидатов через шаблон
    @app.route('/')
    def home_page():
        return render_template('list.html', candidates=load_candidates_from_json())

    # Создание личной страницы каждого кандидата
    @app.route('/candidate/<int:x>')
    def candidate_page(x):
        if 0 < x < len(load_candidates_from_json()) + 1:
            return render_template('single.html', candidate_name=get_candidate(x)['name'],
                                   candidate_position=get_candidate(x)['position'],
                                   img=get_candidate(x)['picture'], candidate_skills=get_candidate(x)['skills'])
        else:
            return "Такого кандидата нет"

    # Поиск совпадений среди кандидатов
    @app.route('/search/<name>')
    def candidates_coincidence(name):
        return render_template('search.html', candidates=get_candidates_by_name(name),
                               length=len(get_candidates_by_name(name)))

    # Поиск кандидатов со скиллом
    @app.route('/skill/<skill_name>')
    def candidate_skills(skill_name):
        return render_template('skill.html', candidates=get_candidates_by_skill(skill_name),
                               length=len(get_candidates_by_skill(skill_name)), skill_name=skill_name)

    app.run()


if __name__ == '__main__':
    main()
