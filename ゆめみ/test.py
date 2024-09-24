import sys
import csv

def main(argv):#起動コマンドhighscore test/in/basic/pre_100.entry.csv test/in/basic/unique_10.score.csv
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.
    mode = argv[0]
    entry_log_file = argv[1]
    score_log_file = argv[2]

    entries = read_csv(entry_log_file)
    scores = read_csv(score_log_file)

    players = [{'id':id,'name':name} for id,name in entries]
    player_scores = [{'id':id,'score':score} for id,score in scores]

    player_map = {player['id']:player for player in players}
    for score in player_scores:
        if score['id'] in player_map:
            player_map['id']['score'] = score['score']

    ranking = sorted(player_map.values(),key=lambda x: x.get('score',0),reverse=True)
    current_rank = 1
    previous_score = ranking[0]['score'] if ranking else 0
    result=[]

    for index,player in enumerate(ranking):
        if player.get('score',0)<previous_score:
            current_rank = index+1
        result.append({'rank':current_rank,'id':player['id'],'name':player['name'],'score':player.get('score',0)})
        previous_score = player.get('score',0)

    print("rank,player_id,handle_name,score")
    for r in result:
        print(f"{r['rank']},{r['id']},{r['name']},{r['score']}")

def read_csv(file_path):
    try:
        with open(file_path,'r',newline='',encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
            print(f"{len(data)},{file_path}")
            return data
    except FileNotFoundError as e:
        print(f"Error reading file {file_path}:{e}")
        return None


if __name__ == '__main__':
    main(sys.argv[1:])
