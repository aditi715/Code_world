def has_duplicate_badges(badge_ids):
    seen_badges = set()

    for b_id in badge_ids:
        if b_id in seen_badges:
            return True
        seen_badges.add(b_id)
        return False
    
    if __name__ == " _main_":
        print(has_duplicate_badges([1,2,3,1]))
        print(has_duplicate_badges([10,20,30]))