var UrlopownikstartWatch;
var UrlopownikstartAccept; //promiss + przeladowanie  z uprawnieniami

app.directive("urlopownik", function () {
    return {
        restrict: "E",
        templateUrl: "/urlopownik/",
        transclude: true
    }
});


function urlopownikControler ($scope) {
    $scope.show = [];
    for (var i = 0; i < 3; i++){
        $scope.show[i]= false;
    }

    $scope.showMenu = function (elementtoshow){
        for (var i = 0; i < $scope.show.length; i++){
            $scope.show[i]= false;
        }
        $scope.show[elementtoshow]= true;
        if (elementtoshow === 2) {
            UrlopownikstartWatch ();
        }
        if (elementtoshow === 1) {
            UrlopownikstartAccept ();
        }
    }
}


function urlopownikRequestController ($scope, $http) {

    $scope.request = {};
    //lista osob mogacych zastapic
    $scope.instant = [];
    $scope.request.who = $scope.instant[0];
    $scope.request.reason = "reason";
    $scope.from = new Date();
    $scope.to = new Date();

    $scope.applyForVacation = function () {
        if (($scope.to < $scope.from) || ($scope.from < new Date())) {
            showError ("Wrong dates, please change data.");
        } else {
            $scope.request.fromday = $scope.from.getDate().toString();
            $scope.request.frommonth =  ($scope.from.getMonth() + 1).toString();
            $scope.request.fromyear = $scope.from.getFullYear().toString();
            $scope.request.today = $scope.to.getDate().toString();
            $scope.request.tomonth = ($scope.to.getMonth() + 1).toString();
            $scope.request.toyear = $scope.to.getFullYear().toString();
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

function urlopownikAcceptController ($scope, $http) {
    $scope.accepting = [];
    $scope.statuses = [];

    //uruchamiane do zobaczenia z roznym statusem!!!
    UrlopownikstartAccept = function () {
        $http({
            method: 'GET',
            url: '/urlopownik/acceptstatus/'
        }).success(function (data) {
            $scope.statuses = data.status;
        }).error (function () {
            showError ("Error occured with connection to the server, please load page again.")
        });
    }

    //lista do zaakceptowania
    $scope.ToAcceptList = function () {
        $http({
            method: 'GET',
            url: '/urlopownik/acceptstart/'
        }).success(function (data) {
            $scope.accepting = [];
            var fromdate;
            var todate;
            for (var i = 0; i < parseInt(data.length); i++){
                fromdate = new Date (data.fromyear[i], data.frommonth[i], data.fromday[i]);
                todate = new Date (data.toyear[i], data.tomonth[i], data.today[i]);
                $scope.accepting.push({fromdate:fromdate, todate:todate, status:"undefined", reason:data.reason[i]});
            }
        }).error (function () {
            showError ("Error occured with connection to the server, please load page again.")
        });
    }


    $scope.UrlopownikAccept = function () {
        $http({
            method: 'POST',
            url: '/urlopownik/accept/',
            data: angular.toJson({cos: "cos"})
        }).success(function (data) {

        }).error (function () {
            showError ("Error occured with connection to the server, please load page again.")
        });
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
