angular.module('expenses', ['infinite-scroll']).config(expensesRouter).config(setSeparator);

function expensesRouter ($routeProvider) { /* no client navigation */ }

function setSeparator ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
}
