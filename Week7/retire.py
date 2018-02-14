import pylab as plt


def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate / 12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1 + mRate) + monthly]
    return base, savings


def display(monthlies, rate, terms):
    plt.figure('Retire Month')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label='Retire:' + str(monthly))
        plt.legend(loc='upper left')
    plt.show()


def displayRates(month, rates, terms):
    plt.figure('Retire Rate')
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals, label='Retire:' + str(month) + ':' + str(int(rate * 100)))
        plt.legend(loc='upper left')
    plt.show()


def displayRatesMonth(monthlies, rates, terms):
    plt.figure('Retire Both')
    plt.clf()
    plt.xlim(30 * 12, 40 * 12)
    monthLabels = ['r', 'b', 'g', 'k']
    rateLabels = ['-', 'o', '-']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i % len(monthLabels)]
        for j in range(len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[j % len(rateLabels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, monthLabel + rateLabel, label='Retire:' + str(monthly) + ':' + str(int(rate * 100)))
            plt.legend(loc='upper left')
    plt.show()


# display([500, 600, 700, 800, 900, 1000, 1100], 0.05, 40 * 12)

# displayRates(800, [.03, .05, .07], 40 * 12)

displayRatesMonth([500, 700, 900, 1100], [.03, .05, .07], 40 * 12)
