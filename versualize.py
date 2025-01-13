# import pandas as pd
# import matplotlib.pyplot as plt

# def loading_cleaning_data(filepath):
#     data = pd.read_csv(filepath)
    
#     print("Available columns in the original file:", data.columns.tolist())
    
#     data = data.dropna()
#     return data

# def normalize_column_names(data):
#     data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_').str.replace(r'[^\w]', '', regex=True)
#     print("Columns after cleaning:", data.columns.tolist())
#     return data

# def find_column(data, column_candidates):

#     for candidate in column_candidates:
#         for col in data.columns:
#             if candidate.lower() in col.lower():
#                 return col
#     return None

# def plotting_column_vs_column(data, column1, column2):
#     if column1 in data.columns and column2 in data.columns:
#         data1 = data[column1]
#         data2 = data[column2]
#         plt.figure(figsize=(10, 6))
#         plt.scatter(data1, data2, alpha=0.6, edgecolor='k')
#         plt.title(f"{column1} vs {column2}", fontsize=14)
#         plt.xlabel(column1, fontsize=12)
#         plt.ylabel(column2, fontsize=12)
#         plt.grid(True)
#         plt.show()
#     else:
#         print(f"One or both columns '{column1}' and '{column2}' not found in the dataset.")

# def process_comparisons(data, base_column_candidates, related_column_candidates):
#     base_column = find_column(data, base_column_candidates)
#     if not base_column:
#         print(f"Base column not found: {base_column_candidates}")
#         return

#     for related_candidate in related_column_candidates:
#         related_column = find_column(data, [related_candidate])
#         if related_column:
#             plotting_column_vs_column(data, base_column, related_column)
#         else:
#             print(f"Related column not found: {related_candidate}")

# def main():
#     filepath = r".\data.csv"
#     data = loading_cleaning_data(filepath)

#     data = normalize_column_names(data)

#     gender_candidates = ["gender"]
#     gender_related_columns = [
#         "what_type_of_video_games_do_you_typically_play",
#         "name_the_video_game_you_usually_play",
#         "how_many_hours_do_you_play_video_games_in_a_day",
#         "how_much_time_do_you_play_violent_video_games_specifically",
#         "if_i_have_to_resort_to_violence_to_protect_my_rights_i_will",
#         "once_i_became_so_mad_i_broke_things",
#         "when_people_disagree_with_me_i_get_into_arguments",
#         "when_i_argue_i_use_abusive_language",
#         "i_am_a_hottempered_person",
#         "do_you_believe_that_playing_violent_video_games_can_lead_to_aggressive_behavior_in_real_life"
#     ]
#     process_comparisons(data, gender_candidates, gender_related_columns)

#     age_candidates = ["age", "what_is_your_age"]
#     age_related_columns = gender_related_columns + [
#         "i_am_suspicious_of_strangers_who_are_too_friendly",
#         "i_have_threatened_some_people_whom_i_know",
#         "have_you_ever_been_involved_in_delinquent_behaviour_like_stealing_breaking_things_of_others"
#     ]
#     process_comparisons(data, age_candidates, age_related_columns)

#     class_candidates = ["class"]
#     process_comparisons(data, class_candidates, age_related_columns)

#     family_candidates = ["type_of_family"]
#     family_related_columns = [
#         "what_type_of_video_games_do_you_typically_play",
#         "name_the_video_game_you_usually_play"
#     ]
#     process_comparisons(data, family_candidates, family_related_columns)

# if __name__ == "__main__":
#     main()


import os 

w = os.open("")

for i in range(1000):
    print("b2aly sana bshtem 3adel")
