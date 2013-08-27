app.directive("urlopownik", function () {
    return {
        restrict: "E",
        templateUrl: "../../../urlopownik/templates/urlopownik/index.html",
        transclude: true
    }
});


function urlopownikControler ($scope) {
    $scope.show = [];
    $scope.request = {};
    $scope.client = [
        {name:"Ktos1", user:"User1"},
        {name:"Ktos2", user:"User2"}
    ];
    $scope.request.who = $scope.client[0];
    $scope.request.from = new Date();
    $scope.request.to = new Date();
    $scope.request.reason = "reason";
    for (var i = 0; i < 3; i++){
        $scope.show[i]= false;
    }

    $scope.from = new Date();
    $scope.to = new Date();


    $scope.showMenu = function (elementtoshow){
        for (var i = 0; i < $scope.show.length; i++){
            $scope.show[i]= false;
        }
        $scope.show[elementtoshow]= true;

    }
    $scope.applyForVacation = function () {
        if ($scope.to < $scope.from){
            showError ("Wrong dates, please change data.");
        } else {
            //$http

        }


    }

}
