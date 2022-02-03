# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def inventory_filter(item_type, inventory):
    
    # 인벤토리에서 특정 종류의 아이템 목록만 반환
    # 함수의 첫 번째 인자는 찾고자 하는 아이템의 종류 (문자열 데이터)
    # 함수의 두 번째 인자는 캐릭터의 현재 인벤토리 정보 (리스트)
    # 인벤토리 리스트에는 아이템들의 정보들이 각각 딕셔너리 데이터로 저장됨
    # 찾고자 하는 종류에 해당하는 아이템(딕셔너리)들로만 구성된 새로운 리스트 반환
    item_list = []
    for element in inventory:
        if element['type'] == item_type:
            item_list.append(element)
    return item_list


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    item_type = 'weapon'
    inventory = [
        {
            'id': 1,
            'name': 'Elder Wand',
            'type': 'weapon',
            'grade': 'legend',
        },
        {
            'id': 2,
            'name': 'Healing Potion',
            'type': 'potion',
            'grade': 'normal',
        },
        {
            'id': 3,
            'name': 'Steel Helmet',
            'type': 'armor',
            'grade': 'rare',
        },
        {
            'id': 4,
            'name': 'Long Sword',
            'type': 'weapon',
            'grade': 'normal',
        },
    ]
    print(inventory_filter(item_type, inventory)) 
    # [{'id': 1, 'name': 'Elder Wand', 'type': 'weapon', 'grade': 'legend'}, {'id': 4, 'name': 'Long Sword', 'type': 'weapon', 'grade': 'normal'}]
