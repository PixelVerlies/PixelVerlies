import map

def dungeonOne():
    all_rooms = []

    all_rooms.append(map.room(0, [
                [1,[2,0],1,[2,2],1,[2,4],1],
                [1,0,1,0,1,0,1],
                [1,0,1,0,1,0,1],
                [1,0,0,3,0,0,1],
                [1,1,1,1,1,1,1]]))
    
    all_rooms.append(map.room(1, [
                [1,1,1,[2,8],1,1,1],
                [1,0,0,0,0,0,1],
                [1,0,[4,1],1,[4,1],0,[2,6]],
                [1,0,0,0,0,0,1],
                [1,1,1,1,[2,1],1,1]]))
    
    all_rooms.append(map.room(2, [
                [1,1,1],
                [[2,7],0,1],
                [1,0,[2,10]],
                [1,[2,3],1]]))
    
    all_rooms.append(map.room(3, [
                [1,1,1,[2,12],1],
                [[2,11],0,0,0,1],
                [1,1,[2,5],1,1]]))
    
    all_rooms.append(map.room(4, [
                [1,1,[2,16],1,1],
                [1,0,0,0,1],
                [1,0,[4,2],[4,1],1],
                [1,0,0,0,1],
                [1,0,0,0,[2,14]],
                [1,[2,9],1,1,1]]))
    
    all_rooms.append(map.room(5, [
                [0,0,0,0,1,[2,18],1],
                [0,0,1,1,1,0,1],
                [1,1,1,0,0,0,1],
                [[2,15],0,0,0,0,0,1],
                [1,1,1,0,0,0,1],
                [0,0,1,1,1,0,1],
                [0,0,0,0,1,[2,13],1]]))
    
    all_rooms.append(map.room(6, [
                [1,1,1,1,1,0,0],
                [1,0,0,0,1,1,1],
                [1,0,[4,3],0,0,0,[2,20]],
                [1,0,0,0,1,1,1],
                [1,1,[2,17],1,1,0,0]]))
    
    all_rooms.append(map.room(7, [
                [1,1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,1],
                [1,0,1,0,[4,3],0,1,0,1],
                [[2,21],0,0,0,0,0,0,0,1],
                [1,0,1,0,0,[4,2],1,0,1],
                [1,[4,3],0,0,0,0,0,0,1],
                [1,1,1,[2,19],1,1,1,1,1],]))

    door_list = []

    door_list.append(map.door(0,0,1,1,1))
    door_list.append(map.door(1,1,0,0,2))

    door_list.append(map.door(2,0,3,2,1))
    door_list.append(map.door(3,2,2,0,2))

    door_list.append(map.door(4,0,5,3,1))
    door_list.append(map.door(5,3,4,0,2))

    door_list.append(map.door(6,1,7,2,4))
    door_list.append(map.door(7,2,6,1,3))

    door_list.append(map.door(8,1,9,4,1))
    door_list.append(map.door(9,4,8,1,2))

    door_list.append(map.door(10,2,11,3,4))
    door_list.append(map.door(11,3,10,2,3))

    door_list.append(map.door(12,3,13,5,1))
    door_list.append(map.door(13,5,12,3,2))

    door_list.append(map.door(14,4,15,5,4))
    door_list.append(map.door(15,5,14,4,3))

    door_list.append(map.door(16,4,17,6,1))
    door_list.append(map.door(17,6,16,4,2))

    door_list.append(map.door(18,5,19,7,1))
    door_list.append(map.door(19,7,18,5,2))

    door_list.append(map.door(20,6,21,7,4))
    door_list.append(map.door(21,7,20,6,3))

    return all_rooms, door_list