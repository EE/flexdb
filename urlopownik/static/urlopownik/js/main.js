var UrlopownikstartWatch;

app.directive("urlopownik", function () {
    return {
        restrict: "E",
        templateUrl: "/urlopownik/",
        transclude: true
    }
});


function urlopownikControler ($scope, $http) {
    $scope.show = [];
    $scope.request = {};
    $scope.client = [
        {name:"Ktos1", user:"User1"},
        {name:"Ktos2", user:"User2"}
    ];
    $scope.request.who = $scope.client[0];
    $scope.request.reason = "reason";
    for (var i = 0; i < 3; i++){
        $scope.show[i]= false;
    }

    // wynik zapytania
    //$scope.result = "";

    $scope.from = new Date();
    $scope.to = new Date();

    $scope.showMenu = function (elementtoshow){
        for (var i = 0; i < $scope.show.length; i++){
            $scope.show[i]= false;
        }
        $scope.show[elementtoshow]= true;
        if (elementtoshow === 2) {
            UrlopownikstartWatch ();
        }

    }
    $scope.applyForVacation = function () {
        if (($scope.to < $scope.from) || ($scope.from < new Date())) {
            showError ("Wrong dates, please change data.");
        } else {
            $scope.request.fromday = $scope.from.getDate().toString();
            $scope.request.frommonth =  ($scope.from.getMonth() + 1).toString();
            $scope.request.fromyear = $scope.from.getFullYear().toString();
            $scope.request.today = $scope.to.getDate().toString();;
            $scope.request.tomonth = ($scope.to.getMonth() + 1).toString();;
            $scope.request.toyear = $scope.to.getFullYear().toString();;
            $http({
                method: 'POST',
                url: '/urlopownik/add/',
                data: angular.toJson($scope.request)
            }).success(function (data) {
                //Przekierowanie lub komunikat

                }).error (function () {
                    showError ("Error occured with connection to the server, please load page again.")
            });

        }

    }

}


function urlopownikWatchController ($scope, $http) {

    $scope.watching = [];

    UrlopownikstartWatch = function () {
        $http({
            method: 'GET',
            url: '/urlopownik/watch/'
        }).success(function (data) {
            $scope.watching = [];
            var fromdate;
            var todate;
            for (var i = 0; i < parseInt(data.length); i++){
                fromdate = new Date (data.fromyear[i], data.frommonth[i], data.fromday[i]);
                todate = new Date (data.toyear[i], data.tomonth[i], data.today[i]);
                $scope.watching.push({fromdate:fromdate, todate:todate, status:"undefined", reason:data.reason[i]});
            }
        }).error (function () {
            showError ("Error occured with connection to the server, please load page again.")
        });


    }
}
