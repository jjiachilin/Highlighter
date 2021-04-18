import json

def text_generator(script):   
    for time in script:
        hold=time['ts'].split(":")
        time['ts'] = [int(hold[0])*60+int(hold[1]),float(hold[2])]

    #reading timestamps
    with open('mock.txt') as timestamps:
        stamps = timestamps.readlines()

    #converting timestamp ts format
    def ts_convert(arr):    
        arr = [i.replace('"','').replace('\n','').split(":") for i in arr]
        arr = [[int(i[0])*60+int(i[1]),float(i[2])] for i in arr]
        return arr 

    stamps = ts_convert(stamps)

    index = 0

    def finding_ts(stamp,id_count):
        while True:
            script_stamp = script[id_count]["ts"]
            if stamp[0]>script_stamp[0]:
                id_count +=1
                continue
            if stamp[0]==script_stamp[0]:
                if stamp[1]>script_stamp[1]:
                    id_count +=1
                    continue
            return id_count

    def upper(stamp,id_count):
        stamp=[stamp[0]+1,stamp[1]]
        while True:
            script_stamp = script[id_count]["ts"]
            if stamp[0]>script_stamp[0]:
                id_count +=1
                continue
            if stamp[0]==script_stamp[0]:
                if stamp[1]>script_stamp[1]:
                    id_count +=1
                    continue
            return id_count

    def lower(stamp,id_count):
        if stamp[0]==0:
            stamp=[0,0]
        else:
            stamp=[stamp[0]-1,stamp[1]]
        while True:
            if id_count <= 0:
                return 0
            script_stamp = script[id_count]["ts"]
            if stamp[0]<script_stamp[0]:
                id_count -=1
                continue
            if stamp[0]==script_stamp[0]:
                if stamp[1]<script_stamp[1]:
                    id_count -=1
                    continue
            return id_count

    '''f = open("highlighted_script.txt", "a")
    f.truncate(0)'''
    arr = []
    for stamp in stamps:
        index = finding_ts(stamp,index)
        low = lower(stamp,index)
        high = upper(stamp,index)
        '''f.write()
        f.write("Highlighted Time: " + str(stamp[0]) + ' minutes and '+ str(stamp[1])+' seconds.\n'+
        "Time Range: "+ str(script[low]['ts'][0]) + ' minutes and '+ str(script[low]['ts'][1])+' seconds ~ '+
        str(script[high]['ts'][0]) + ' minutes and '+ str(script[high]['ts'][1])+' seconds.'+'\n\n')'''
        empty = []
        for i in range(low,high+1):
            empty.append(script[i]['text'])
        arr.append("".join(empty))

    return arr


    '''f.write('\n\n')
    f.close()'''
if __name__ == "__main__":
    with open("transcript.json") as f:
        transcript = json.load(f)
        print(text_generator(transcript))