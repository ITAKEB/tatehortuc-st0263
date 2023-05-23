from mrjob.job import MRJob


class CompaniesDataAnalityc(MRJob):

    def mapper(self, _, line):
        company = line.split(',')[0]
        price = line.split(',')[1]
        date = line.split(',')[2]

        if date != "date" and price != "price" and company != "Company":
            yield f"{company} min-day:", [date, price]
            yield f"{company} max-day:", [date, price]
            yield f"{company} actions-list:", price
            yield "black-day", [date, price]

    def reducer(self, key, values):
        minor = 0
        maxim = 0

        if key.__contains__('max-day'):
            maxim = max(values, key=lambda x: (x[1]))

            yield key, maxim

        if key.__contains__('min-day'):
            minor = min(values, key=lambda x: (x[1]))

            yield key, minor

        if key.__contains__('actions-list'):
            action = key.split(" ")[0]
            prev = -1
            cont = 0
            length = 0
            aux = False
            for price in values:
                length = length + 1
                if float(price) >= prev:
                    prev = float(price)
                    cont = cont + 1
            if (cont == length):
                aux = True
            if aux:
                yield "good action", action

        if key.__contains__('black-day'):
            days = sorted(values, key=lambda x: (x[1]))

            yield "black-day", days[0][0]


if __name__ == '__main__':
    CompaniesDataAnalityc.run()
