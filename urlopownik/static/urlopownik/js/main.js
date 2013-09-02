var Urlopownikstart = [];
app.directive("urlopownik", function () {
    return {
        restrict: "E",
        templateUrl: templates_dict['urlopownik'][0],
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
        Urlopownikstart[elementtoshow] ();
        $scope.show[elementtoshow]= true;

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
    $scope.sendrequest = false;
    $scope.failedrequest = false;

    Urlopownikstart[0] = function () {
        $scope.sendrequest = false;
        $scope.failedrequest = false;
    };

    $scope.applyForVacation = function () {
        if (($scope.to < $scope.from) || ($scope.from < new Date(new Date().setDate(new Date().getDate()-1)))) {
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
                if (data.ok === true){
                        $scope.sendrequest = true;
                        $scope.failedrequest = false;

                    } else {
                        $scope.sendrequest = false;
                        $scope.failedrequest = true;
                    }
                }).error (function () {
                    showError ("Error occured with connection to the server, please load page again.")
            });
        }
    };
}

function urlopownikAcceptController ($scope, $http) {
    $scope.accepting = [];
    $scope.statuses = [];
    $scope.search = {};
    $scope.searchstatus;
    $scope.find = [];
    $scope.statusval = [];

    //uruchamiane do zobaczenia z roznym statusem!!!
    Urlopownikstart[1] = function () {
        $http({
            method: 'GET',
            url: '/urlopownik/acceptstatus/'
        }).success(function (data) {
            $scope.statuses = data.status;
        }).error (function () {
            showError ("Error occured with connection to the server, please load page again.")
        });
    };

    $scope.UrlopownikFind = function () {
        $http({
            method: 'POST',
            url: '/urlopownik/acceptfind/',
            data: angular.toJson({searchstatus: $scope.searchstatus})
        }).success(function (data) {
            $scope.find = [];
            $scope.statusval = [];
            var fromdate;
            var todate;
            for (var i = 0; i < parseInt(data.length); i++) {
                fromdate = new Date(data.fromyear[i], data.frommonth[i], data.fromday[i]);
                todate = new Date(data.toyear[i], data.tomonth[i], data.today[i]);
                $scope.statusval[data.pk[i]] = data.status;
                $scope.find.push({
                    fromdate: fromdate,
                    todate: todate,
                    status: data.status,
                    reason: data.reason[i],
                    user: data.user[i],
                    pk: data.pk[i]
                });
            }
        }).error (function () {
            showError ("Error occured with connection to the server, please load page again.")
        });

    };


    $scope.UrlopownikChange = function (number, it) {
        $http({
            method: 'POST',
            url: '/urlopownik/changestatus/',
            data: angular.toJson({
                status: $scope.statusval [number],
                pk: number
            })
        }).success(function (data) {
                //if ok i czy sie zmienilo
            $scope.find.splice( it, 1 );
        }).error (function () {
            showError ("Error occured with connection to the server, please load page again.")
        });
    };

}


function urlopownikWatchController ($scope, $http) {

    $scope.watching = [];

    Urlopownikstart[2] = function () {
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


    };
}
