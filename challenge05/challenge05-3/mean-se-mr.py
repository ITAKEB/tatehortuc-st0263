from mrjob.job import MRJob

class EmploysDataAnalityc(MRJob):

    def mapper(self, _, line):
        employ = line.split(',')[0] 
        sector = line.split(',')[1] 
        salary = line.split(',')[2] 

        if salary != "salary":
            yield sector, int(salary)

        if employ != "idemp":
            yield employ, int(salary)
            
        if sector != "sector" and employ != "idemp":
            yield f'sector-employ {sector}', employ



    def reducer(self, key, values):
        count = 0
        total = 0

        if key.__contains__('sector-employ'):
            for value in values:
                count += 1

            yield key, count
        else:
            for value in values:
                total += value
                count += 1

            average = total / count
            yield key, average


if __name__ == '__main__':
    EmploysDataAnalityc.run()

