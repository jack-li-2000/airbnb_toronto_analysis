import pandas as pd

# helper function to put every row in a column into a single list, one list for each column

def unique_id_df_rev(id):
    current = rev[rev['listing_id'] == id]

    columns = list(rev.columns)
    columns.pop(0)

    return [list(current[col].values) for col in columns]

# example

# unique_id_df(1419, rev)

# quick and dirty to get map working with different df
def unique_id_df_cal(id):
    current = cal[cal['listing_id'] == id]

    columns = list(cal.columns)
    columns.pop(0)

    return [list(current[col].values) for col in columns]

if __name__ == "__main__":

    cal = pd.read_csv('calendar.csv')
    lis = pd.read_csv('listings.csv')
    rev = pd.read_csv('reviews.csv')

    rev_uni_list_id = list(rev['listing_id'].unique())
    rev_total_content = list(map(unique_id_df_rev, rev_uni_list_id))

    cal_uni_list_id = list(cal['listing_id'].unique())
    cal_total_content = list(map(unique_id_df_cal, cal_uni_list_id))

    rev_old_columns = list(rev.columns)
    rev_old_columns.pop(0)

    cal_old_columns = list(cal.columns)
    cal_old_columns.pop(0)

    rev_df = pd.DataFrame(rev_total_content, columns=rev_old_columns)
    rev_df['listing_id'] = rev_uni_list_id

    cal_df = pd.DataFrame(cal_total_content, columns=cal_old_columns)
    cal_df['listing_id'] = cal_uni_list_id

    lis.rename(columns={'id': 'listing_id'},inplace=True)
    new1 = lis.merge(cal_df, how= 'left', on=['listing_id'])
    final_df = new1.merge(rev_df, how= 'left', on=['listing_id'])

    final_df.to_csv('airbnb_toronto.csv')