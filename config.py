#configuration
import os
CONFIG ={
        'district':'서울특별시',
        'contries':[('중국', 112), ('일본', 130), ('미국', 275)],
        'common':{
          #  'service_key':'O4GTUjJhqd2Zh%2FUKol%2FD%2F03SF57S%2B1Kr%2FEF55PYYb3zh0ZeimbMRClwaUBScosK6KGB7rJHgnlr4QCF%2FIpTV1Q%3D%3D',
            'start_year':2017,
            'end_year':2017,
            'fetch':True,
            'result_directory':'__results__/crawling'
        }
}
if not os.path.exists(CONFIG['common']['result_directory']):
    os.makedirs(CONFIG['common']['result_directory'])