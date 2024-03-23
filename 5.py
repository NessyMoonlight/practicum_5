def F(w):
    categories = {
        w < 16: 'выраженный дефицит массы тела',
        16 <= w < 18.49: 'недостаточная масса тела',
        18.5 <= w < 24.99: 'норма',
        25 <= w < 29.99: 'избыточная масса тела',
        30 <= w < 34.99: 'ожирение первой степени',
        35 <= w < 39.99: 'ожирение второй степени',
        40 <= w: 'ожирение третьей степени'
    }

    for key in categories:
        if key:
            return categories[key]

weight = int(input())
height = int(input())

imt = round((weight / height ** 2) * 703, 2)

print(F(imt))