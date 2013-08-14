angular.module('flexdb', []).
  config(function($interpolateProvider){
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  });


function tableControll ($scope){
    $scope.users = [
        {Lname:'Walt', Fname:'Kowalsky', Email: 'Walt@walt.org', Country: 'USA', Addres: 'New Jersey' }
        ];


    $scope.addUser = function() {
        $scope.users.push({
            Lname:$scope.Lname,
            Fname:$scope.Fname,
            Email:$scope.Email,
            Country:$scope.Country,
            Addres:$scope.Addres
        });

        $scope.Lname = '';
        $scope.Fname = '';
        $scope.Email = '';
        $scope.Country = '';
        $scope.Addres = '';
    };

}
