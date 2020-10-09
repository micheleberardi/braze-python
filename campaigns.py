import requests

def data_series(token,campaign_id):
    header = {"Authorization": "Bearer " + str(token)}
    endpoint = "https://rest.iad-03.braze.com/campaigns/data_series?campaign_id="+campaign_id+"&length=7&ending_at=2010-10-08T23:59:59-5:00"
    post = requests.get(endpoint,headers=header)
    return post.json()

def campaigns_list(token):
    header = {"Authorization": "Bearer " + str(token)}
    endpoint = "https://rest.iad-03.braze.com/campaigns/list?page=0&include_archived=false&sort_direction=desc"
    post = requests.get(endpoint,headers=header)
    return post.json()

def campaigns_details(token, campaign_id):
    header = {"Authorization": "Bearer " + str(token)}
    endpoint = "https://rest.iad-03.braze.com/campaigns/details?campaign_id="+campaign_id
    post = requests.get(endpoint,headers=header)
    return post.json()



if __name__ == '__main__':
    
    token = '111111111-2222-3333-4444-22222222'
    campaign_id = 'aaaaaaaa-bbbb-cccc-dddd-eeeeeeeee'
    
    data_series = data_series(token,campaign_id)        #### https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaign_analytics/
    details = campaigns_details(token, campaign_id)     #### https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaign_details/
    list = campaigns_list(token)                        #### https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaigns/
