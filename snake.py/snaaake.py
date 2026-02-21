
seg = []

while run:
    try:
        sc.update()

        # wall collision
        if abs(h.xcor()) > 290 or abs(h.ycor()) > 290:
            time.sleep(1)
            h.goto(0, 0)
            h.direction = "Stop"

            for segment in seg:
                segment.goto(1000, 1000)
            seg.clear()

            s = 0
            d = 0.1
            p.clear()

            p.write(f"Score : {s}  High Score : {hs}", align="center", font=("candara", 24, "bold"))

        # food collision
        if h.distance(f) < 20:
            f.goto(random.randint(-270, 270), random.randint(-270, 270))
            new_seg = t.Turtle()
            new_seg.shape("square")
            new_seg.color("orange")
            new_seg.penup()
            seg.append(new_seg)
            d -= 0.001
            s += 10

            if s > hs:
                hs = s
            p.clear()
            p.write(f"Score : {s}  High Score : {hs}", align="center", font=("candara", 24, "bold"))

        # move body
        for i in range(len(seg) - 1, 0, -1):
            x = seg[i - 1].xcor()
            y = seg[i - 1].ycor()
            seg[i].goto(x, y)

        if seg:
            seg[0].goto(h.xcor(), h.ycor())
        move()

        # self collision
        for segment in seg:
            if segment.distance(h) < 20:
                time.sleep(1)
                h.goto(0, 0)
                h.direction = "Stop"

                for segment in seg:
                    segment.goto(1000, 1000)
                seg.clear()

                s = 0
                d = 0.1
                p.clear()
                p.write(f"Score : {s}  High Score : {hs}", align="center", font=("candara", 24, "bold"))

        time.sleep(d)
        
    except t.Terminator:
        run = False
