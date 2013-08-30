var app = angular.module("flexdb", []);
var chosenApp;
var showError;
var showModal;

app.config(function ($interpolateProvider, $httpProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

app.directive("errorhandle", function () {
    return {
        restrict: "E",
        scope: {
            errorname: '@'
        },
        templateUrl: "/error/",
        transclude: true
    }
});

function overallAppControler($scope, $http, $compile) {
    $scope.apps = {};
    $scope.data = {};
    $scope.user_URL = "";
    $scope.logged = false;
    $scope.applist = true;


    $scope.ajaxDone = function (data) {
        if (data != null) {
            if (data.username != null) {
                $scope.data.username = data.username;
            }
            if (data.first_name != null) {
                $scope.data.first_name = data.first_name;
            }
            if (data.last_name != null) {
                $scope.data.last_name = data.last_name;
            }
            if (data.email != null) {
                $scope.data.email = data.email;
            }
        }
    };


    function loadUserData() {
        $http({
            method: 'GET',
            url: '/accounts/users/'
        }).success(function (data) {
                if ((data != null) && (data[0] != null)) {
                    $scope.ajaxDone(data[0]);
                    if (data[0].url != null) {
                        $scope.user_URL = data[0].url;
                        $scope.logged = true;
                    }
                }
            }).error(function () {
                showError("Error occured with connection to the server, please load page again.")
            });
    }

    $scope.appClick = function (appName) {
        var newElement = $compile("<" + appName + ">" + "</" + appName + ">")($scope);
        chosenApp(newElement);
        $scope.applist = false;
    };

    $scope.goToAppsList = function () {
        chosenApp(null);
        $scope.applist = true;
    };

    loadUserData();
}

function mainAppControler($element) {
    chosenApp = function (el) {
        $element.children(0).remove();
        if (el != null) {
            $element.append(el);
        }
    };
}

function modalControll($scope, $element, $compile) {

    showModal = function (el, attr) {
        var newElement = $compile("<" + el + " " + attr + ">" + "</" + el + ">")($scope);
        $element.children(0).remove();
        if (newElement != null) {
            $element.append(newElement);
            $element.modal('show');
        }
    };


    showError = function (errorvalue) {
        showModal('errorhandle', 'errorname = "' + errorvalue + '"');
    };
}
