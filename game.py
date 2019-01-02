import numpy as np
import pandas as pd
import pymysql

USERNAME = "hackathonmike"
PASSWORD = 'HACKathon123'
HOST = "db4free.net"
DATABASE = "itchackathon"


def run_query(query):
    con = pymysql.connect(host=HOST, user=USERNAME,
                          password=PASSWORD, database=DATABASE)
    try:
        result = pd.read_sql(query, con)
    except TypeError:
        print('It was update or insert')
        result = None
    con.commit()
    con.close()
    return result


def get_img_shows():
    # pull from db
    query = "select img_id, shows from game"
    return run_query(query)


def calculate_inverse_prob(df):
    df['inv'] = df["shows"].max(axis=0) + 1 - df['shows']
    df['prob'] = df['inv'] / df['inv'].sum()
    return df


def choose_pictures(df):
    return np.random.choice(df['img_id'], replace=False, size=2, p=df['prob'])


def get_imgs():
    df = get_img_shows()
    df = calculate_inverse_prob(df)
    img_id1, img_id2 = choose_pictures(df)
    return img_id1, img_id2


def voting(options):
    options = [str(option) for option in options]
    votes = dict(zip(options, np.zeros(len(options))))

    # returns both img_ids and the score of one
    valid_input = False
    # GET USER INPUT INITIAL
    while not valid_input:
        vote = input(
            "Who do you vote to be the MDU - Miss Dog Universe today?\n\nChoose between {}\n".format(
                " and ".join(options)))
        # GET USER INPUT INITIAL
        if vote in options:
            valid_input = True
            votes[vote] = 1

    return votes


def store_result(vote):
    # Update shows
    query_update_shows = "UPDATE game SET shows = shows + 1 WHERE id in ({})".format(", ".join(vote.keys()))
    run_query(query_update_shows)

    # Update score
    voted = list(vote.keys())[np.argmax(vote.values())]
    query_update_score = "UPDATE game SET score = score + 1 WHERE id in ({})".format(voted)
    run_query(query_update_score)
    # print(voted)


def get_the_king():
    # get the one with the biggest percentage of votes
    # print on the screen

    ## NEED TO INNER JOIN IMAGE TABLE AND RETURN THE PATH OF THE IMAGE

    query = """select klev.img_name, game.score/game.shows as points,  avg(game.shows) as avg_views
from game inner join klev on image.id = game.img_id
where game.shows > (select avg(shows) from game)*3/4
order by points desc 
limit 1"""


def main():
    img_id1, img_id2 = get_imgs()
    vote = voting([img_id1, img_id2])
    store_result(vote)


if __name__ == '__main__':
    main()
