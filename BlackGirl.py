import getter
import pandas as ps
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter
from collections import Counter
getter.download("https://github.com/mathiasjepsen/PythonDatasetAssignment/raw/master/ks-projects-201801.csv")
filename = "ks-projects-201801.csv"
data = ps.read_csv(filename)
matrix = data.as_matrix()
def question_1():
    # print(matrix[1,:])
    cat_dict_all = {}
    cat_dict_succes = {}
    # first a dictionary is created to get the amount of main categories
    for cat in data['main_category'].values:
        try:
            cat_dict_all[cat] += 1
        except:
            cat_dict_all[cat] = 1
    # second yet another dictionary is made to get the amount of categories that were actually succesful
    for i in range(len(data)):
        try:
            if (matrix[i, 9] == "successful"):
                cat_dict_succes[matrix[i, 3]] += 1
        except:
            cat_dict_succes[matrix[i, 3]] = 1

    # run through a dictionary and divide the succes with the amount to get a succesrate and update a dict with the new value.
    for key in cat_dict_all.keys():
        cat_dict_succes[key] = cat_dict_succes[key] / cat_dict_all[key]

    plt.bar(cat_dict_succes.keys(), cat_dict_succes.values())
    plt.show()


def question_2():
    mask = matrix[:, 3] == "Dance"
    sorted_matrix = matrix[mask]
    dict_dance = {}
    # we made a filtered matrix that only has the data with main category "Dance"
    # Lets make fucking dictionary, and plot that bitch!!!
    #Tjalfes counter !!!!!
    #print(Counter(sorted_matrix[:,2]))

    for dancer in sorted_matrix[:]:
        try:
            dict_dance[dancer[2]] += 1
        except:
            dict_dance[dancer[2]] = 1

    plt.bar(dict_dance.keys(), dict_dance.values())
    plt.show()


def question_3():
    pledged_arr = matrix[1:, 13]
    index = (len(pledged_arr) + 1) / 2
    median = 0.0
    if index % 10 == 0.5:
        index = int(index)
        median = (pledged_arr[index] + pledged_arr[index + 1] / 2)
    else:
        index = int(index)
        median = (pledged_arr[index] / 2)
    print("the median is:", median)


def question_4():



    mask = (matrix[:, 9] == "successful") & (matrix[:, 13] > 5000)

    sorted_matrix = matrix[mask]
    sorted_matrix = matrix[(matrix[:, 9] == "successful") & (matrix[:, 13] > 5000)]

    dict = {}
    for stuff in sorted_matrix:
        try:
            dict[stuff[2]] += 1
        except:
            dict[stuff[2]] = 1

    sorted_from_dict = sorted(dict.items(), key=itemgetter(1), reverse=True)

    top_five = sorted_from_dict[0:5]
    labels = []
    sizes = []
    for item in top_five:
        labels.append(item[0])
        sizes.append(item[1])


    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, autopct=make_autopct(sizes),
            shadow=True, startangle=90)
    ax1.axis('equal')
    patches, texts = plt.pie(sizes, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.show()


# just a helper 'method' to turn percent into a value. Notice the "my_autopct" input value pct... where the hell does that come from ?  is that autogenerated from autopct ???
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)

    return my_autopct


def question_5():
    # Lets create a dataframe to work with
    df = ps.DataFrame(data)

    # Then lets subtract the column names we need
    cats = list(df.columns.values)
    main_cat = cats[3]
    name = cats[1]
    goal = cats[6]
    curr = cats[4]
    state = cats[9]

    # We also want the names of main categories
    areas = df.main_category.unique()

    # Now select the only the needed rows and columns
    new_set = df.loc[(df[state] == 'successful') & (df[curr] == 'USD'), [name, main_cat, goal, curr, state]]

    # Lets sort from high to low by our goal
    sorted_set = new_set.sort_values(by=[main_cat, goal], ascending=False)

    # Then lets sorted subtracts by main category
    publish = sorted_set.loc[sorted_set[main_cat] == areas[0]]
    films = sorted_set.loc[sorted_set[main_cat] == areas[1]]
    music = sorted_set.loc[sorted_set[main_cat] == areas[2]]
    food = sorted_set.loc[sorted_set[main_cat] == areas[3]]
    design = sorted_set.loc[sorted_set[main_cat] == areas[4]]
    crafts = sorted_set.loc[sorted_set[main_cat] == areas[5]]
    games = sorted_set.loc[sorted_set[main_cat] == areas[6]]
    comics = sorted_set.loc[sorted_set[main_cat] == areas[7]]
    fashion = sorted_set.loc[sorted_set[main_cat] == areas[8]]
    theater = sorted_set.loc[sorted_set[main_cat] == areas[9]]
    art = sorted_set.loc[sorted_set[main_cat] == areas[10]]
    photo = sorted_set.loc[sorted_set[main_cat] == areas[11]]
    tech = sorted_set.loc[sorted_set[main_cat] == areas[12]]
    dance = sorted_set.loc[sorted_set[main_cat] == areas[13]]
    jour = sorted_set.loc[sorted_set[main_cat] == areas[14]]

    # For full precise answering, lets print all categories and goals
    print(games.iloc[0][goal], games.iloc[-1][goal], games.iloc[0][main_cat] + ": " + games.iloc[0][name])
    print(films.iloc[0][goal], films.iloc[-1][goal], films.iloc[0][main_cat] + ": " + films.iloc[0][name])
    print(tech.iloc[0][goal], tech.iloc[-1][goal], tech.iloc[0][main_cat] + ": " + tech.iloc[0][name])
    print(design.iloc[0][goal], design.iloc[-1][goal], design.iloc[0][main_cat] + ": " + design.iloc[0][name])
    print(art.iloc[0][goal], art.iloc[-1][goal], art.iloc[0][main_cat] + ": " + art.iloc[0][name])
    print(photo.iloc[0][goal], photo.iloc[-1][goal], photo.iloc[0][main_cat] + ": " + photo.iloc[0][name])
    print(food.iloc[0][goal], food.iloc[-1][goal], food.iloc[0][main_cat] + ": " + food.iloc[0][name])
    print(fashion.iloc[0][goal], fashion.iloc[-1][goal], fashion.iloc[0][main_cat] + ": " + fashion.iloc[0][name])
    print(comics.iloc[0][goal], comics.iloc[-1][goal], comics.iloc[0][main_cat] + ": " + comics.iloc[0][name])
    print(publish.iloc[0][goal], publish.iloc[-1][goal], publish.iloc[0][main_cat] + ": " + publish.iloc[0][name])
    print(music.iloc[0][goal], music.iloc[-1][goal], music.iloc[0][main_cat] + ": " + music.iloc[0][name])
    print(theater.iloc[0][goal], theater.iloc[-1][goal], theater.iloc[0][main_cat] + ": " + theater.iloc[0][name])
    print(jour.iloc[0][goal], jour.iloc[-1][goal], jour.iloc[0][main_cat] + ": " + jour.iloc[0][name])
    print(dance.iloc[0][goal], dance.iloc[-1][goal], dance.iloc[0][main_cat] + ": " + dance.iloc[0][name])
    print(crafts.iloc[0][goal], crafts.iloc[-1][goal], crafts.iloc[0][main_cat] + ": " + crafts.iloc[0][name])

    # We are done data-grinding, lets show the results
    top_cats = [
        games.iloc[0][main_cat] + ": " + games.iloc[0][name],
        films.iloc[0][main_cat] + ": " + films.iloc[0][name],
        tech.iloc[0][main_cat] + ": " + tech.iloc[0][name],
        design.iloc[0][main_cat] + ": " + design.iloc[0][name],
        art.iloc[0][main_cat] + ": " + art.iloc[0][name]
    ]

    top_goals = [
        games.iloc[0][goal],
        films.iloc[0][goal],
        tech.iloc[0][goal],
        design.iloc[0][goal],
        art.iloc[0][goal]
    ]

    y_pos = np.arange(len(top_cats))
    plt.barh(y_pos, top_goals)
    plt.yticks(y_pos, top_cats)
    plt.xlabel('Goal in USD')
    plt.title('Top 5 - Most successfully funded projects by goal-amount range')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    question_1()
    question_2()
    question_3()
    question_4()
    question_5()
