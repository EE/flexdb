app.directive("urlopownik", function () {
    return {
        restrict: "E",
        templateUrl: "../../../urlopownik/templates/urlopownik/index.html",
        transclude: true
    }
});


function urlopownikControler ($scope) {
    $scope.show = [];
    $scope.show[0]= false;
    $scope.show[1]= false;
    $scope.show[2]= false;


    $scope.showMenu = function (elementtoshow){
        for (var i = 0; i < $scope.show.length; i++){
            $scope.show[i]= false;
        }
        $scope.show[elementtoshow]= true;

    }

}
