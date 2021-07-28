from enum import Enum
from typing import List, Union, Optional
from uuid import UUID


class Action(Enum):
    CANCEL = "Cancel"
    CREATE = "Create"


class AddressListType(Enum):
    STRING = "String"


class AddressList:
    address: List[str]
    type: AddressListType

    def __init__(self, address: List[str], type: AddressListType) -> None:
        self.address = address
        self.type = type


class Allowconsumption(Enum):
    NO = "No"
    YES = "Yes"


class Ledgername(Enum):
    E_SALES_LOCAL_GST = "E-Sales - Local (GST)"
    SALES_LOCAL_GST = "Sales - Local (GST)"
    SALES_OMS_GST = "Sales - OMS (GST)"


class OldauditentryidsListType(Enum):
    NUMBER = "Number"


class OldauditentryidsList:
    oldauditentryids: int
    type: OldauditentryidsListType

    def __init__(self, oldauditentryids: int, type: OldauditentryidsListType) -> None:
        self.oldauditentryids = oldauditentryids
        self.type = type


class SERVICETAXDETAILSLISTClass:
    applicablefrom: int
    isreverseapplicable: Allowconsumption
    isnegativelistservice: Allowconsumption
    useforisd: Allowconsumption
    isrecipientliab: Allowconsumption

    def __init__(self, applicablefrom: int, isreverseapplicable: Allowconsumption, isnegativelistservice: Allowconsumption, useforisd: Allowconsumption, isrecipientliab: Allowconsumption) -> None:
        self.applicablefrom = applicablefrom
        self.isreverseapplicable = isreverseapplicable
        self.isnegativelistservice = isnegativelistservice
        self.useforisd = useforisd
        self.isrecipientliab = isrecipientliab


class AccountingallocationsList:
    oldauditentryids_list: OldauditentryidsList
    ledgername: Ledgername
    gstclass: str
    isdeemedpositive: Allowconsumption
    ledgerfromitem: Allowconsumption
    removezeroentries: Allowconsumption
    ispartyledger: Allowconsumption
    islastdeemedpositive: Allowconsumption
    iscapvattaxaltered: Allowconsumption
    iscapvatnotclaimed: Allowconsumption
    amount: str
    servicetaxdetails_list: Union[SERVICETAXDETAILSLISTClass, str]
    bankallocations_list: str
    billallocations_list: str
    interestcollection_list: str
    oldauditentries_list: str
    accountauditentries_list: str
    auditentries_list: str
    inputcrallocs_list: str
    dutyheaddetails_list: str
    excisedutyheaddetails_list: str
    ratedetails_list: str
    summaryallocs_list: str
    stpymtdetails_list: str
    excisepaymentallocations_list: str
    taxbillallocations_list: str
    taxobjectallocations_list: str
    tdsexpenseallocations_list: str
    vatstatutorydetails_list: str
    costtrackallocations_list: str
    refvoucherdetails_list: str
    invoicewisedetails_list: str
    vatitcdetails_list: str
    advancetaxdetails_list: str
    classrate: Optional[str]

    def __init__(self, oldauditentryids_list: OldauditentryidsList, ledgername: Ledgername, gstclass: str, isdeemedpositive: Allowconsumption, ledgerfromitem: Allowconsumption, removezeroentries: Allowconsumption, ispartyledger: Allowconsumption, islastdeemedpositive: Allowconsumption, iscapvattaxaltered: Allowconsumption, iscapvatnotclaimed: Allowconsumption, amount: str, servicetaxdetails_list: Union[SERVICETAXDETAILSLISTClass, str], bankallocations_list: str, billallocations_list: str, interestcollection_list: str, oldauditentries_list: str, accountauditentries_list: str, auditentries_list: str, inputcrallocs_list: str, dutyheaddetails_list: str, excisedutyheaddetails_list: str, ratedetails_list: str, summaryallocs_list: str, stpymtdetails_list: str, excisepaymentallocations_list: str, taxbillallocations_list: str, taxobjectallocations_list: str, tdsexpenseallocations_list: str, vatstatutorydetails_list: str, costtrackallocations_list: str, refvoucherdetails_list: str, invoicewisedetails_list: str, vatitcdetails_list: str, advancetaxdetails_list: str, classrate: Optional[str]) -> None:
        self.oldauditentryids_list = oldauditentryids_list
        self.ledgername = ledgername
        self.gstclass = gstclass
        self.isdeemedpositive = isdeemedpositive
        self.ledgerfromitem = ledgerfromitem
        self.removezeroentries = removezeroentries
        self.ispartyledger = ispartyledger
        self.islastdeemedpositive = islastdeemedpositive
        self.iscapvattaxaltered = iscapvattaxaltered
        self.iscapvatnotclaimed = iscapvatnotclaimed
        self.amount = amount
        self.servicetaxdetails_list = servicetaxdetails_list
        self.bankallocations_list = bankallocations_list
        self.billallocations_list = billallocations_list
        self.interestcollection_list = interestcollection_list
        self.oldauditentries_list = oldauditentries_list
        self.accountauditentries_list = accountauditentries_list
        self.auditentries_list = auditentries_list
        self.inputcrallocs_list = inputcrallocs_list
        self.dutyheaddetails_list = dutyheaddetails_list
        self.excisedutyheaddetails_list = excisedutyheaddetails_list
        self.ratedetails_list = ratedetails_list
        self.summaryallocs_list = summaryallocs_list
        self.stpymtdetails_list = stpymtdetails_list
        self.excisepaymentallocations_list = excisepaymentallocations_list
        self.taxbillallocations_list = taxbillallocations_list
        self.taxobjectallocations_list = taxobjectallocations_list
        self.tdsexpenseallocations_list = tdsexpenseallocations_list
        self.vatstatutorydetails_list = vatstatutorydetails_list
        self.costtrackallocations_list = costtrackallocations_list
        self.refvoucherdetails_list = refvoucherdetails_list
        self.invoicewisedetails_list = invoicewisedetails_list
        self.vatitcdetails_list = vatitcdetails_list
        self.advancetaxdetails_list = advancetaxdetails_list
        self.classrate = classrate


class BasicuserdescriptionList:
    basicuserdescription: Optional[str]
    type: AddressListType

    def __init__(self, basicuserdescription: Optional[str], type: AddressListType) -> None:
        self.basicuserdescription = basicuserdescription
        self.type = type


class Name(Enum):
    WARE_HOUSE_MANKOLI_BHIWANDI = "Ware -House (Mankoli-Bhiwandi)"


class P(Enum):
    THE_1_JUL_2020 = "1-Jul-2020"
    THE_26_JUN_2020 = "26-Jun-2020"
    THE_30_DAYS = "30 Days"


class Orderduedate:
    jd: int
    p: P
    text: P

    def __init__(self, jd: int, p: P, text: P) -> None:
        self.jd = jd
        self.p = p
        self.text = text


class Orderno(Enum):
    EMPTY = ""
    SSI20_21_PI_028 = "SSI20-21/PI-028"
    SSI20_21_PI_029 = "SSI20-21/PI-029"
    SSI20_21_PI_030 = "SSI20-21/PI-030"


class BatchallocationsList:
    godownname: Name
    batchname: str
    destinationgodownname: Optional[Name]
    indentno: str
    orderno: Orderno
    trackingnumber: str
    dynamiccstiscleared: Allowconsumption
    amount: str
    actualqty: str
    billedqty: str
    orderduedate: Optional[Orderduedate]
    additionaldetails_list: str
    vouchercomponentlist_list: str
    inclvatrate: Optional[str]

    def __init__(self, godownname: Name, batchname: str, destinationgodownname: Optional[Name], indentno: str, orderno: Orderno, trackingnumber: str, dynamiccstiscleared: Allowconsumption, amount: str, actualqty: str, billedqty: str, orderduedate: Optional[Orderduedate], additionaldetails_list: str, vouchercomponentlist_list: str, inclvatrate: Optional[str]) -> None:
        self.godownname = godownname
        self.batchname = batchname
        self.destinationgodownname = destinationgodownname
        self.indentno = indentno
        self.orderno = orderno
        self.trackingnumber = trackingnumber
        self.dynamiccstiscleared = dynamiccstiscleared
        self.amount = amount
        self.actualqty = actualqty
        self.billedqty = billedqty
        self.orderduedate = orderduedate
        self.additionaldetails_list = additionaldetails_list
        self.vouchercomponentlist_list = vouchercomponentlist_list
        self.inclvatrate = inclvatrate


class ALLINVENTORYENTRIESLISTElement:
    basicuserdescription_list: BasicuserdescriptionList
    stockitemname: str
    isdeemedpositive: Allowconsumption
    islastdeemedpositive: Allowconsumption
    isautonegate: Allowconsumption
    iscustomsclearance: Allowconsumption
    istrackcomponent: Allowconsumption
    istrackproduction: Allowconsumption
    isprimaryitem: Allowconsumption
    isscrap: Allowconsumption
    rate: str
    amount: str
    actualqty: str
    billedqty: str
    batchallocations_list: BatchallocationsList
    accountingallocations_list: AccountingallocationsList
    dutyheaddetails_list: str
    supplementarydutyheaddetails_list: str
    taxobjectallocations_list: str
    refvoucherdetails_list: str
    exciseallocations_list: str
    expenseallocations_list: str
    mrprate: Optional[str]
    inclvatrate: Optional[str]

    def __init__(self, basicuserdescription_list: BasicuserdescriptionList, stockitemname: str, isdeemedpositive: Allowconsumption, islastdeemedpositive: Allowconsumption, isautonegate: Allowconsumption, iscustomsclearance: Allowconsumption, istrackcomponent: Allowconsumption, istrackproduction: Allowconsumption, isprimaryitem: Allowconsumption, isscrap: Allowconsumption, rate: str, amount: str, actualqty: str, billedqty: str, batchallocations_list: BatchallocationsList, accountingallocations_list: AccountingallocationsList, dutyheaddetails_list: str, supplementarydutyheaddetails_list: str, taxobjectallocations_list: str, refvoucherdetails_list: str, exciseallocations_list: str, expenseallocations_list: str, mrprate: Optional[str], inclvatrate: Optional[str]) -> None:
        self.basicuserdescription_list = basicuserdescription_list
        self.stockitemname = stockitemname
        self.isdeemedpositive = isdeemedpositive
        self.islastdeemedpositive = islastdeemedpositive
        self.isautonegate = isautonegate
        self.iscustomsclearance = iscustomsclearance
        self.istrackcomponent = istrackcomponent
        self.istrackproduction = istrackproduction
        self.isprimaryitem = isprimaryitem
        self.isscrap = isscrap
        self.rate = rate
        self.amount = amount
        self.actualqty = actualqty
        self.billedqty = billedqty
        self.batchallocations_list = batchallocations_list
        self.accountingallocations_list = accountingallocations_list
        self.dutyheaddetails_list = dutyheaddetails_list
        self.supplementarydutyheaddetails_list = supplementarydutyheaddetails_list
        self.taxobjectallocations_list = taxobjectallocations_list
        self.refvoucherdetails_list = refvoucherdetails_list
        self.exciseallocations_list = exciseallocations_list
        self.expenseallocations_list = expenseallocations_list
        self.mrprate = mrprate
        self.inclvatrate = inclvatrate


class SList:
    basicuserdescription_list: Optional[BasicuserdescriptionList]
    stockitemname: str
    isdeemedpositive: Allowconsumption
    islastdeemedpositive: Allowconsumption
    isautonegate: Allowconsumption
    iscustomsclearance: Allowconsumption
    istrackcomponent: Allowconsumption
    istrackproduction: Allowconsumption
    isprimaryitem: Allowconsumption
    isscrap: Allowconsumption
    rate: str
    amount: str
    actualqty: str
    billedqty: str
    batchallocations_list: BatchallocationsList
    accountingallocations_list: Optional[AccountingallocationsList]
    dutyheaddetails_list: str
    supplementarydutyheaddetails_list: str
    taxobjectallocations_list: str
    refvoucherdetails_list: str
    exciseallocations_list: str
    expenseallocations_list: str
    costtrackallocations_list: Optional[str]

    def __init__(self, basicuserdescription_list: Optional[BasicuserdescriptionList], stockitemname: str, isdeemedpositive: Allowconsumption, islastdeemedpositive: Allowconsumption, isautonegate: Allowconsumption, iscustomsclearance: Allowconsumption, istrackcomponent: Allowconsumption, istrackproduction: Allowconsumption, isprimaryitem: Allowconsumption, isscrap: Allowconsumption, rate: str, amount: str, actualqty: str, billedqty: str, batchallocations_list: BatchallocationsList, accountingallocations_list: Optional[AccountingallocationsList], dutyheaddetails_list: str, supplementarydutyheaddetails_list: str, taxobjectallocations_list: str, refvoucherdetails_list: str, exciseallocations_list: str, expenseallocations_list: str, costtrackallocations_list: Optional[str]) -> None:
        self.basicuserdescription_list = basicuserdescription_list
        self.stockitemname = stockitemname
        self.isdeemedpositive = isdeemedpositive
        self.islastdeemedpositive = islastdeemedpositive
        self.isautonegate = isautonegate
        self.iscustomsclearance = iscustomsclearance
        self.istrackcomponent = istrackcomponent
        self.istrackproduction = istrackproduction
        self.isprimaryitem = isprimaryitem
        self.isscrap = isscrap
        self.rate = rate
        self.amount = amount
        self.actualqty = actualqty
        self.billedqty = billedqty
        self.batchallocations_list = batchallocations_list
        self.accountingallocations_list = accountingallocations_list
        self.dutyheaddetails_list = dutyheaddetails_list
        self.supplementarydutyheaddetails_list = supplementarydutyheaddetails_list
        self.taxobjectallocations_list = taxobjectallocations_list
        self.refvoucherdetails_list = refvoucherdetails_list
        self.exciseallocations_list = exciseallocations_list
        self.expenseallocations_list = expenseallocations_list
        self.costtrackallocations_list = costtrackallocations_list


class Chequecrosscomment(Enum):
    A_C_PAYEE = "A/c Payee"


class Instrumentnumber(Enum):
    CMS = "CMS"


class Paymentmode(Enum):
    TRANSACTED = "Transacted"


class Transactiontype(Enum):
    INTER_BANK_TRANSFER = "Inter Bank Transfer"
    OTHERS = "Others"


class Transfermode(Enum):
    NEFT = "NEFT"
    RTGS = "RTGS"


class BANKALLOCATIONSLISTClass:
    date: int
    instrumentdate: int
    bankersdate: int
    name: UUID
    transactiontype: Transactiontype
    paymentfavouring: str
    transfermode: Optional[Transfermode]
    uniquereferencenumber: str
    status: Allowconsumption
    paymentmode: Paymentmode
    bankpartyname: str
    isconnectedpayment: Allowconsumption
    issplit: Allowconsumption
    iscontractused: Allowconsumption
    isacceptedwithwarning: Allowconsumption
    istransforced: Allowconsumption
    chequeprinted: Optional[int]
    amount: str
    contractdetails_list: str
    bankstatusinfo_list: str
    chequecrosscomment: Optional[Chequecrosscomment]
    instrumentnumber: Optional[Instrumentnumber]
    secondarystatus: Optional[str]

    def __init__(self, date: int, instrumentdate: int, bankersdate: int, name: UUID, transactiontype: Transactiontype, paymentfavouring: str, transfermode: Optional[Transfermode], uniquereferencenumber: str, status: Allowconsumption, paymentmode: Paymentmode, bankpartyname: str, isconnectedpayment: Allowconsumption, issplit: Allowconsumption, iscontractused: Allowconsumption, isacceptedwithwarning: Allowconsumption, istransforced: Allowconsumption, chequeprinted: Optional[int], amount: str, contractdetails_list: str, bankstatusinfo_list: str, chequecrosscomment: Optional[Chequecrosscomment], instrumentnumber: Optional[Instrumentnumber], secondarystatus: Optional[str]) -> None:
        self.date = date
        self.instrumentdate = instrumentdate
        self.bankersdate = bankersdate
        self.name = name
        self.transactiontype = transactiontype
        self.paymentfavouring = paymentfavouring
        self.transfermode = transfermode
        self.uniquereferencenumber = uniquereferencenumber
        self.status = status
        self.paymentmode = paymentmode
        self.bankpartyname = bankpartyname
        self.isconnectedpayment = isconnectedpayment
        self.issplit = issplit
        self.iscontractused = iscontractused
        self.isacceptedwithwarning = isacceptedwithwarning
        self.istransforced = istransforced
        self.chequeprinted = chequeprinted
        self.amount = amount
        self.contractdetails_list = contractdetails_list
        self.bankstatusinfo_list = bankstatusinfo_list
        self.chequecrosscomment = chequecrosscomment
        self.instrumentnumber = instrumentnumber
        self.secondarystatus = secondarystatus


class Billtype(Enum):
    AGST_REF = "Agst Ref"
    NEW_REF = "New Ref"


class BILLALLOCATIONSLISTElement:
    name: str
    billtype: Billtype
    tdsdeducteeisspecialrate: Allowconsumption
    amount: str
    interestcollection_list: str
    stbillcategories_list: str
    billcreditperiod: Optional[Orderduedate]

    def __init__(self, name: str, billtype: Billtype, tdsdeducteeisspecialrate: Allowconsumption, amount: str, interestcollection_list: str, stbillcategories_list: str, billcreditperiod: Optional[Orderduedate]) -> None:
        self.name = name
        self.billtype = billtype
        self.tdsdeducteeisspecialrate = tdsdeducteeisspecialrate
        self.amount = amount
        self.interestcollection_list = interestcollection_list
        self.stbillcategories_list = stbillcategories_list
        self.billcreditperiod = billcreditperiod


class CostcentreallocationsList:
    name: str
    amount: str

    def __init__(self, name: str, amount: str) -> None:
        self.name = name
        self.amount = amount


class CategoryallocationsList:
    category: str
    isdeemedpositive: Allowconsumption
    costcentreallocations_list: CostcentreallocationsList

    def __init__(self, category: str, isdeemedpositive: Allowconsumption, costcentreallocations_list: CostcentreallocationsList) -> None:
        self.category = category
        self.isdeemedpositive = isdeemedpositive
        self.costcentreallocations_list = costcentreallocations_list


class AllledgerentriesList:
    oldauditentryids_list: OldauditentryidsList
    ledgername: str
    gstclass: str
    isdeemedpositive: Allowconsumption
    ledgerfromitem: Allowconsumption
    removezeroentries: Allowconsumption
    ispartyledger: Allowconsumption
    islastdeemedpositive: Allowconsumption
    iscapvattaxaltered: Allowconsumption
    iscapvatnotclaimed: Allowconsumption
    amount: str
    vatexpamount: str
    servicetaxdetails_list: str
    bankallocations_list: Union[BANKALLOCATIONSLISTClass, str]
    billallocations_list: Union[List[BILLALLOCATIONSLISTElement], BILLALLOCATIONSLISTElement, str]
    interestcollection_list: str
    oldauditentries_list: str
    accountauditentries_list: str
    auditentries_list: str
    inputcrallocs_list: str
    dutyheaddetails_list: str
    excisedutyheaddetails_list: str
    ratedetails_list: str
    summaryallocs_list: str
    stpymtdetails_list: str
    excisepaymentallocations_list: str
    taxbillallocations_list: str
    taxobjectallocations_list: str
    tdsexpenseallocations_list: str
    vatstatutorydetails_list: str
    costtrackallocations_list: Optional[str]
    refvoucherdetails_list: str
    invoicewisedetails_list: str
    vatitcdetails_list: str
    advancetaxdetails_list: str
    categoryallocations_list: Optional[CategoryallocationsList]
    inventoryallocations_list: Optional[SList]

    def __init__(self, oldauditentryids_list: OldauditentryidsList, ledgername: str, gstclass: str, isdeemedpositive: Allowconsumption, ledgerfromitem: Allowconsumption, removezeroentries: Allowconsumption, ispartyledger: Allowconsumption, islastdeemedpositive: Allowconsumption, iscapvattaxaltered: Allowconsumption, iscapvatnotclaimed: Allowconsumption, amount: str, vatexpamount: str, servicetaxdetails_list: str, bankallocations_list: Union[BANKALLOCATIONSLISTClass, str], billallocations_list: Union[List[BILLALLOCATIONSLISTElement], BILLALLOCATIONSLISTElement, str], interestcollection_list: str, oldauditentries_list: str, accountauditentries_list: str, auditentries_list: str, inputcrallocs_list: str, dutyheaddetails_list: str, excisedutyheaddetails_list: str, ratedetails_list: str, summaryallocs_list: str, stpymtdetails_list: str, excisepaymentallocations_list: str, taxbillallocations_list: str, taxobjectallocations_list: str, tdsexpenseallocations_list: str, vatstatutorydetails_list: str, costtrackallocations_list: Optional[str], refvoucherdetails_list: str, invoicewisedetails_list: str, vatitcdetails_list: str, advancetaxdetails_list: str, categoryallocations_list: Optional[CategoryallocationsList], inventoryallocations_list: Optional[SList]) -> None:
        self.oldauditentryids_list = oldauditentryids_list
        self.ledgername = ledgername
        self.gstclass = gstclass
        self.isdeemedpositive = isdeemedpositive
        self.ledgerfromitem = ledgerfromitem
        self.removezeroentries = removezeroentries
        self.ispartyledger = ispartyledger
        self.islastdeemedpositive = islastdeemedpositive
        self.iscapvattaxaltered = iscapvattaxaltered
        self.iscapvatnotclaimed = iscapvatnotclaimed
        self.amount = amount
        self.vatexpamount = vatexpamount
        self.servicetaxdetails_list = servicetaxdetails_list
        self.bankallocations_list = bankallocations_list
        self.billallocations_list = billallocations_list
        self.interestcollection_list = interestcollection_list
        self.oldauditentries_list = oldauditentries_list
        self.accountauditentries_list = accountauditentries_list
        self.auditentries_list = auditentries_list
        self.inputcrallocs_list = inputcrallocs_list
        self.dutyheaddetails_list = dutyheaddetails_list
        self.excisedutyheaddetails_list = excisedutyheaddetails_list
        self.ratedetails_list = ratedetails_list
        self.summaryallocs_list = summaryallocs_list
        self.stpymtdetails_list = stpymtdetails_list
        self.excisepaymentallocations_list = excisepaymentallocations_list
        self.taxbillallocations_list = taxbillallocations_list
        self.taxobjectallocations_list = taxobjectallocations_list
        self.tdsexpenseallocations_list = tdsexpenseallocations_list
        self.vatstatutorydetails_list = vatstatutorydetails_list
        self.costtrackallocations_list = costtrackallocations_list
        self.refvoucherdetails_list = refvoucherdetails_list
        self.invoicewisedetails_list = invoicewisedetails_list
        self.vatitcdetails_list = vatitcdetails_list
        self.advancetaxdetails_list = advancetaxdetails_list
        self.categoryallocations_list = categoryallocations_list
        self.inventoryallocations_list = inventoryallocations_list


class Teredby(Enum):
    PROBIKE = "probike"
    TEREDBY_PROBIKE = "PROBIKE"


class BasicbuyeraddressList:
    basicbuyeraddress: List[str]
    type: AddressListType

    def __init__(self, basicbuyeraddress: List[str], type: AddressListType) -> None:
        self.basicbuyeraddress = basicbuyeraddress
        self.type = type


class BasicordertermsList:
    basicorderterms: List[str]
    type: AddressListType

    def __init__(self, basicorderterms: List[str], type: AddressListType) -> None:
        self.basicorderterms = basicorderterms
        self.type = type


class Addresstype(Enum):
    ADDRESSTYPE_DELIVERY_ADDRESS = "DELIVERY ADDRESS"
    DELIVERY_ADDRESS = "Delivery Address"
    NEW_STORE = "New Store"


class Classname(Enum):
    E_SALES_LOCAL = "E-Sales Local"
    GST_SALES_LOCAL = "GST Sales Local"
    GST_SALES_OMS = "GST Sales OMS"


class Countryofresidence(Enum):
    INDIA = "India"


class ConsigneeaddressList:
    consigneeaddress: Union[List[str], str]
    type: AddressListType

    def __init__(self, consigneeaddress: Union[List[str], str], type: AddressListType) -> None:
        self.consigneeaddress = consigneeaddress
        self.type = type


class ConsignoraddressList:
    consignoraddress: List[str]
    type: AddressListType

    def __init__(self, consignoraddress: List[str], type: AddressListType) -> None:
        self.consignoraddress = consignoraddress
        self.type = type


class GSTREGISTRATIONTYPEEnum(Enum):
    REGULAR = "Regular"


class TransportdetailsList:
    transportmode: str
    vehicletype: GSTREGISTRATIONTYPEEnum
    ignorevehiclenovalidation: Allowconsumption

    def __init__(self, transportmode: str, vehicletype: GSTREGISTRATIONTYPEEnum, ignorevehiclenovalidation: Allowconsumption) -> None:
        self.transportmode = transportmode
        self.vehicletype = vehicletype
        self.ignorevehiclenovalidation = ignorevehiclenovalidation


class EWAYBILLDETAILSLISTClass:
    consignoraddress_list: ConsignoraddressList
    consigneeaddress_list: ConsigneeaddressList
    documenttype: str
    consigneegstin: str
    consigneestatename: str
    consigneepincode: int
    subtype: str
    consignorname: str
    consignorpincode: int
    consignorgstin: str
    consignorstatename: str
    consigneename: str
    shippedfromstate: str
    shippedtostate: str
    ignoregstinvalidation: Allowconsumption
    transportdetails_list: TransportdetailsList
    consigneeaddresstype: Optional[Addresstype]

    def __init__(self, consignoraddress_list: ConsignoraddressList, consigneeaddress_list: ConsigneeaddressList, documenttype: str, consigneegstin: str, consigneestatename: str, consigneepincode: int, subtype: str, consignorname: str, consignorpincode: int, consignorgstin: str, consignorstatename: str, consigneename: str, shippedfromstate: str, shippedtostate: str, ignoregstinvalidation: Allowconsumption, transportdetails_list: TransportdetailsList, consigneeaddresstype: Optional[Addresstype]) -> None:
        self.consignoraddress_list = consignoraddress_list
        self.consigneeaddress_list = consigneeaddress_list
        self.documenttype = documenttype
        self.consigneegstin = consigneegstin
        self.consigneestatename = consigneestatename
        self.consigneepincode = consigneepincode
        self.subtype = subtype
        self.consignorname = consignorname
        self.consignorpincode = consignorpincode
        self.consignorgstin = consignorgstin
        self.consignorstatename = consignorstatename
        self.consigneename = consigneename
        self.shippedfromstate = shippedfromstate
        self.shippedtostate = shippedtostate
        self.ignoregstinvalidation = ignoregstinvalidation
        self.transportdetails_list = transportdetails_list
        self.consigneeaddresstype = consigneeaddresstype


class Fbtpaymenttype(Enum):
    DEFAULT = "Default"


class Vouchertypename(Enum):
    E_SALES = "E-Sales"
    JOURNAL = "Journal"
    PAYMENT = "Payment"
    RECEIPT = "Receipt"
    SALES = "Sales"
    SALES_ORDER = "Sales Order"


class INVOICEORDERLISTLISTClass:
    basicorderdate: int
    ordertype: Vouchertypename
    basicpurchaseorderno: Orderno

    def __init__(self, basicorderdate: int, ordertype: Vouchertypename, basicpurchaseorderno: Orderno) -> None:
        self.basicorderdate = basicorderdate
        self.ordertype = ordertype
        self.basicpurchaseorderno = basicpurchaseorderno


class Methodtype(Enum):
    AS_TOTAL_AMOUNT_ROUNDING = "As Total Amount Rounding"
    AS_USER_DEFINED_VALUE = "As User Defined Value"
    GST = "GST"


class Roundtype(Enum):
    EMPTY = ""
    NORMAL_ROUNDING = "Normal Rounding"


class LEDGERENTRIESLISTElement:
    oldauditentryids_list: OldauditentryidsList
    ledgername: str
    gstclass: str
    isdeemedpositive: Allowconsumption
    ledgerfromitem: Allowconsumption
    removezeroentries: Allowconsumption
    ispartyledger: Allowconsumption
    islastdeemedpositive: Allowconsumption
    iscapvattaxaltered: Allowconsumption
    iscapvatnotclaimed: Allowconsumption
    amount: str
    servicetaxdetails_list: str
    bankallocations_list: str
    billallocations_list: Union[BILLALLOCATIONSLISTElement, str]
    interestcollection_list: str
    oldauditentries_list: str
    accountauditentries_list: str
    auditentries_list: str
    inputcrallocs_list: str
    dutyheaddetails_list: str
    excisedutyheaddetails_list: str
    ratedetails_list: str
    summaryallocs_list: str
    stpymtdetails_list: str
    excisepaymentallocations_list: str
    taxbillallocations_list: str
    taxobjectallocations_list: str
    tdsexpenseallocations_list: str
    vatstatutorydetails_list: str
    costtrackallocations_list: str
    refvoucherdetails_list: str
    invoicewisedetails_list: str
    vatitcdetails_list: str
    advancetaxdetails_list: str
    vatexpamount: Optional[str]
    roundtype: Optional[Roundtype]
    methodtype: Optional[Methodtype]

    def __init__(self, oldauditentryids_list: OldauditentryidsList, ledgername: str, gstclass: str, isdeemedpositive: Allowconsumption, ledgerfromitem: Allowconsumption, removezeroentries: Allowconsumption, ispartyledger: Allowconsumption, islastdeemedpositive: Allowconsumption, iscapvattaxaltered: Allowconsumption, iscapvatnotclaimed: Allowconsumption, amount: str, servicetaxdetails_list: str, bankallocations_list: str, billallocations_list: Union[BILLALLOCATIONSLISTElement, str], interestcollection_list: str, oldauditentries_list: str, accountauditentries_list: str, auditentries_list: str, inputcrallocs_list: str, dutyheaddetails_list: str, excisedutyheaddetails_list: str, ratedetails_list: str, summaryallocs_list: str, stpymtdetails_list: str, excisepaymentallocations_list: str, taxbillallocations_list: str, taxobjectallocations_list: str, tdsexpenseallocations_list: str, vatstatutorydetails_list: str, costtrackallocations_list: str, refvoucherdetails_list: str, invoicewisedetails_list: str, vatitcdetails_list: str, advancetaxdetails_list: str, vatexpamount: Optional[str], roundtype: Optional[Roundtype], methodtype: Optional[Methodtype]) -> None:
        self.oldauditentryids_list = oldauditentryids_list
        self.ledgername = ledgername
        self.gstclass = gstclass
        self.isdeemedpositive = isdeemedpositive
        self.ledgerfromitem = ledgerfromitem
        self.removezeroentries = removezeroentries
        self.ispartyledger = ispartyledger
        self.islastdeemedpositive = islastdeemedpositive
        self.iscapvattaxaltered = iscapvattaxaltered
        self.iscapvatnotclaimed = iscapvatnotclaimed
        self.amount = amount
        self.servicetaxdetails_list = servicetaxdetails_list
        self.bankallocations_list = bankallocations_list
        self.billallocations_list = billallocations_list
        self.interestcollection_list = interestcollection_list
        self.oldauditentries_list = oldauditentries_list
        self.accountauditentries_list = accountauditentries_list
        self.auditentries_list = auditentries_list
        self.inputcrallocs_list = inputcrallocs_list
        self.dutyheaddetails_list = dutyheaddetails_list
        self.excisedutyheaddetails_list = excisedutyheaddetails_list
        self.ratedetails_list = ratedetails_list
        self.summaryallocs_list = summaryallocs_list
        self.stpymtdetails_list = stpymtdetails_list
        self.excisepaymentallocations_list = excisepaymentallocations_list
        self.taxbillallocations_list = taxbillallocations_list
        self.taxobjectallocations_list = taxobjectallocations_list
        self.tdsexpenseallocations_list = tdsexpenseallocations_list
        self.vatstatutorydetails_list = vatstatutorydetails_list
        self.costtrackallocations_list = costtrackallocations_list
        self.refvoucherdetails_list = refvoucherdetails_list
        self.invoicewisedetails_list = invoicewisedetails_list
        self.vatitcdetails_list = vatitcdetails_list
        self.advancetaxdetails_list = advancetaxdetails_list
        self.vatexpamount = vatexpamount
        self.roundtype = roundtype
        self.methodtype = methodtype


class View(Enum):
    ACCOUNTING_VOUCHER_VIEW = "Accounting Voucher View"
    INVOICE_VOUCHER_VIEW = "Invoice Voucher View"


class Typeofexcisevoucher(Enum):
    NON_EXCISE = "Non-Excise"


class Voucher:
    oldauditentryids_list: Optional[OldauditentryidsList]
    date: int
    referencedate: Optional[int]
    guid: str
    narration: Optional[str]
    vouchertypename: Vouchertypename
    reference: Optional[str]
    vouchernumber: str
    partyledgername: Optional[str]
    cstformissuetype: str
    cstformrecvtype: str
    persistedview: Optional[View]
    vchgstclass: str
    enteredby: Teredby
    diffactualqty: Allowconsumption
    ismstfromsync: Allowconsumption
    asoriginal: Allowconsumption
    audited: Allowconsumption
    forjobcosting: Allowconsumption
    isoptional: Allowconsumption
    effectivedate: int
    useforexcise: Allowconsumption
    isforjobworkin: Allowconsumption
    allowconsumption: Allowconsumption
    useforinterest: Allowconsumption
    useforgainloss: Allowconsumption
    useforgodowntransfer: Allowconsumption
    useforcompound: Allowconsumption
    useforservicetax: Allowconsumption
    isexcisevoucher: Allowconsumption
    excisetaxoverride: Allowconsumption
    usefortaxunittransfer: Allowconsumption
    ignoreposvalidation: Allowconsumption
    exciseopening: Allowconsumption
    useforfinalproduction: Allowconsumption
    istdsoverridden: Allowconsumption
    istcsoverridden: Allowconsumption
    istdstcscashvch: Allowconsumption
    includeadvpymtvch: Allowconsumption
    issubworkscontract: Allowconsumption
    isvatoverridden: Allowconsumption
    ignoreorigvchdate: Allowconsumption
    isvatpaidatcustoms: Allowconsumption
    isdeclaredtocustoms: Allowconsumption
    isservicetaxoverridden: Allowconsumption
    isisdvoucher: Allowconsumption
    isexciseoverridden: Allowconsumption
    isexcisesupplyvch: Allowconsumption
    isgstoverridden: Allowconsumption
    gstnotexported: Allowconsumption
    ignoregstinvalidation: Allowconsumption
    isvatprincipalaccount: Allowconsumption
    isboenotapplicable: Allowconsumption
    isshippingwithinstate: Allowconsumption
    isoverseastouristtrans: Allowconsumption
    isdesignatedzoneparty: Allowconsumption
    iscancelled: Allowconsumption
    hascashflow: Allowconsumption
    ispostdated: Allowconsumption
    usetrackingnumber: Allowconsumption
    isinvoice: Allowconsumption
    mfgjournal: Allowconsumption
    hasdiscounts: Allowconsumption
    aspayslip: Allowconsumption
    iscostcentre: Allowconsumption
    isstxnonrealizedvch: Allowconsumption
    isexcisemanufactureron: Allowconsumption
    isblankcheque: Allowconsumption
    isvoid: Allowconsumption
    isonhold: Allowconsumption
    orderlinestatus: Allowconsumption
    vatisagnstcancsales: Allowconsumption
    vatispurcexempted: Allowconsumption
    isvatrestaxinvoice: Allowconsumption
    vatisassesablecalcvch: Allowconsumption
    isvatdutypaid: Allowconsumption
    isdeliverysameasconsignee: Allowconsumption
    isdispatchsameasconsignor: Allowconsumption
    isdeleted: Allowconsumption
    changevchmode: Allowconsumption
    alterid: int
    masterid: int
    voucherkey: str
    excludedtaxations_list: str
    oldauditentries_list: str
    accountauditentries_list: str
    auditentries_list: str
    dutyheaddetails_list: str
    supplementarydutyheaddetails_list: str
    ewaybilldetails_list: Union[EWAYBILLDETAILSLISTClass, str]
    invoicedelnotes_list: str
    invoiceorderlist_list: Union[INVOICEORDERLISTLISTClass, str]
    invoiceindentlist_list: str
    attendanceentries_list: str
    originvoicedetails_list: str
    invoiceexportlist_list: str
    allledgerentries_list: Optional[List[AllledgerentriesList]]
    payrollmodeofpayment_list: str
    attdrecords_list: str
    gstewayconsignoraddress_list: str
    gstewayconsigneeaddress_list: str
    tempgstratedetails_list: str
    remoteid: str
    vchkey: str
    vchtype: Vouchertypename
    action: Action
    objview: View
    fbtpaymenttype: Optional[Fbtpaymenttype]
    address_list: Optional[AddressList]
    basicbuyeraddress_list: Optional[BasicbuyeraddressList]
    basicorderterms_list: Optional[BasicordertermsList]
    alteredon: Optional[int]
    statename: Optional[str]
    alteredby: Optional[Teredby]
    countryofresidence: Optional[Countryofresidence]
    partygstin: Optional[str]
    partyname: Optional[str]
    basicbasepartyname: Optional[str]
    typeofexcisevoucher: Optional[Typeofexcisevoucher]
    placeofsupply: Optional[str]
    consigneegstin: Optional[str]
    basicbuyername: Optional[str]
    basicduedateofpymt: Optional[str]
    consigneepinnumber: Optional[str]
    consigneestatename: Optional[str]
    ledgerentries_list: Union[List[LEDGERENTRIESLISTElement], None, str]
    allinventoryentries_list: Union[List[ALLINVENTORYENTRIESLISTElement], SList, None, str]
    classname: Optional[Classname]
    consigneecstnumber: Optional[str]
    buyerscstnumber: Optional[str]
    basicdatetimeofinvoice: Optional[str]
    basicdatetimeofremoval: Optional[str]
    gstregistrationtype: Optional[GSTREGISTRATIONTYPEEnum]
    vatdealertype: Optional[GSTREGISTRATIONTYPEEnum]
    buyeraddresstype: Optional[Addresstype]
    taxunitname: Optional[Name]

    def __init__(self, oldauditentryids_list: Optional[OldauditentryidsList], date: int, referencedate: Optional[int], guid: str, narration: Optional[str], vouchertypename: Vouchertypename, reference: Optional[str], vouchernumber: str, partyledgername: Optional[str], cstformissuetype: str, cstformrecvtype: str, persistedview: Optional[View], vchgstclass: str, enteredby: Teredby, diffactualqty: Allowconsumption, ismstfromsync: Allowconsumption, asoriginal: Allowconsumption, audited: Allowconsumption, forjobcosting: Allowconsumption, isoptional: Allowconsumption, effectivedate: int, useforexcise: Allowconsumption, isforjobworkin: Allowconsumption, allowconsumption: Allowconsumption, useforinterest: Allowconsumption, useforgainloss: Allowconsumption, useforgodowntransfer: Allowconsumption, useforcompound: Allowconsumption, useforservicetax: Allowconsumption, isexcisevoucher: Allowconsumption, excisetaxoverride: Allowconsumption, usefortaxunittransfer: Allowconsumption, ignoreposvalidation: Allowconsumption, exciseopening: Allowconsumption, useforfinalproduction: Allowconsumption, istdsoverridden: Allowconsumption, istcsoverridden: Allowconsumption, istdstcscashvch: Allowconsumption, includeadvpymtvch: Allowconsumption, issubworkscontract: Allowconsumption, isvatoverridden: Allowconsumption, ignoreorigvchdate: Allowconsumption, isvatpaidatcustoms: Allowconsumption, isdeclaredtocustoms: Allowconsumption, isservicetaxoverridden: Allowconsumption, isisdvoucher: Allowconsumption, isexciseoverridden: Allowconsumption, isexcisesupplyvch: Allowconsumption, isgstoverridden: Allowconsumption, gstnotexported: Allowconsumption, ignoregstinvalidation: Allowconsumption, isvatprincipalaccount: Allowconsumption, isboenotapplicable: Allowconsumption, isshippingwithinstate: Allowconsumption, isoverseastouristtrans: Allowconsumption, isdesignatedzoneparty: Allowconsumption, iscancelled: Allowconsumption, hascashflow: Allowconsumption, ispostdated: Allowconsumption, usetrackingnumber: Allowconsumption, isinvoice: Allowconsumption, mfgjournal: Allowconsumption, hasdiscounts: Allowconsumption, aspayslip: Allowconsumption, iscostcentre: Allowconsumption, isstxnonrealizedvch: Allowconsumption, isexcisemanufactureron: Allowconsumption, isblankcheque: Allowconsumption, isvoid: Allowconsumption, isonhold: Allowconsumption, orderlinestatus: Allowconsumption, vatisagnstcancsales: Allowconsumption, vatispurcexempted: Allowconsumption, isvatrestaxinvoice: Allowconsumption, vatisassesablecalcvch: Allowconsumption, isvatdutypaid: Allowconsumption, isdeliverysameasconsignee: Allowconsumption, isdispatchsameasconsignor: Allowconsumption, isdeleted: Allowconsumption, changevchmode: Allowconsumption, alterid: int, masterid: int, voucherkey: str, excludedtaxations_list: str, oldauditentries_list: str, accountauditentries_list: str, auditentries_list: str, dutyheaddetails_list: str, supplementarydutyheaddetails_list: str, ewaybilldetails_list: Union[EWAYBILLDETAILSLISTClass, str], invoicedelnotes_list: str, invoiceorderlist_list: Union[INVOICEORDERLISTLISTClass, str], invoiceindentlist_list: str, attendanceentries_list: str, originvoicedetails_list: str, invoiceexportlist_list: str, allledgerentries_list: Optional[List[AllledgerentriesList]], payrollmodeofpayment_list: str, attdrecords_list: str, gstewayconsignoraddress_list: str, gstewayconsigneeaddress_list: str, tempgstratedetails_list: str, remoteid: str, vchkey: str, vchtype: Vouchertypename, action: Action, objview: View, fbtpaymenttype: Optional[Fbtpaymenttype], address_list: Optional[AddressList], basicbuyeraddress_list: Optional[BasicbuyeraddressList], basicorderterms_list: Optional[BasicordertermsList], alteredon: Optional[int], statename: Optional[str], alteredby: Optional[Teredby], countryofresidence: Optional[Countryofresidence], partygstin: Optional[str], partyname: Optional[str], basicbasepartyname: Optional[str], typeofexcisevoucher: Optional[Typeofexcisevoucher], placeofsupply: Optional[str], consigneegstin: Optional[str], basicbuyername: Optional[str], basicduedateofpymt: Optional[str], consigneepinnumber: Optional[str], consigneestatename: Optional[str], ledgerentries_list: Union[List[LEDGERENTRIESLISTElement], None, str], allinventoryentries_list: Union[List[ALLINVENTORYENTRIESLISTElement], SList, None, str], classname: Optional[Classname], consigneecstnumber: Optional[str], buyerscstnumber: Optional[str], basicdatetimeofinvoice: Optional[str], basicdatetimeofremoval: Optional[str], gstregistrationtype: Optional[GSTREGISTRATIONTYPEEnum], vatdealertype: Optional[GSTREGISTRATIONTYPEEnum], buyeraddresstype: Optional[Addresstype], taxunitname: Optional[Name]) -> None:
        self.oldauditentryids_list = oldauditentryids_list
        self.date = date
        self.referencedate = referencedate
        self.guid = guid
        self.narration = narration
        self.vouchertypename = vouchertypename
        self.reference = reference
        self.vouchernumber = vouchernumber
        self.partyledgername = partyledgername
        self.cstformissuetype = cstformissuetype
        self.cstformrecvtype = cstformrecvtype
        self.persistedview = persistedview
        self.vchgstclass = vchgstclass
        self.enteredby = enteredby
        self.diffactualqty = diffactualqty
        self.ismstfromsync = ismstfromsync
        self.asoriginal = asoriginal
        self.audited = audited
        self.forjobcosting = forjobcosting
        self.isoptional = isoptional
        self.effectivedate = effectivedate
        self.useforexcise = useforexcise
        self.isforjobworkin = isforjobworkin
        self.allowconsumption = allowconsumption
        self.useforinterest = useforinterest
        self.useforgainloss = useforgainloss
        self.useforgodowntransfer = useforgodowntransfer
        self.useforcompound = useforcompound
        self.useforservicetax = useforservicetax
        self.isexcisevoucher = isexcisevoucher
        self.excisetaxoverride = excisetaxoverride
        self.usefortaxunittransfer = usefortaxunittransfer
        self.ignoreposvalidation = ignoreposvalidation
        self.exciseopening = exciseopening
        self.useforfinalproduction = useforfinalproduction
        self.istdsoverridden = istdsoverridden
        self.istcsoverridden = istcsoverridden
        self.istdstcscashvch = istdstcscashvch
        self.includeadvpymtvch = includeadvpymtvch
        self.issubworkscontract = issubworkscontract
        self.isvatoverridden = isvatoverridden
        self.ignoreorigvchdate = ignoreorigvchdate
        self.isvatpaidatcustoms = isvatpaidatcustoms
        self.isdeclaredtocustoms = isdeclaredtocustoms
        self.isservicetaxoverridden = isservicetaxoverridden
        self.isisdvoucher = isisdvoucher
        self.isexciseoverridden = isexciseoverridden
        self.isexcisesupplyvch = isexcisesupplyvch
        self.isgstoverridden = isgstoverridden
        self.gstnotexported = gstnotexported
        self.ignoregstinvalidation = ignoregstinvalidation
        self.isvatprincipalaccount = isvatprincipalaccount
        self.isboenotapplicable = isboenotapplicable
        self.isshippingwithinstate = isshippingwithinstate
        self.isoverseastouristtrans = isoverseastouristtrans
        self.isdesignatedzoneparty = isdesignatedzoneparty
        self.iscancelled = iscancelled
        self.hascashflow = hascashflow
        self.ispostdated = ispostdated
        self.usetrackingnumber = usetrackingnumber
        self.isinvoice = isinvoice
        self.mfgjournal = mfgjournal
        self.hasdiscounts = hasdiscounts
        self.aspayslip = aspayslip
        self.iscostcentre = iscostcentre
        self.isstxnonrealizedvch = isstxnonrealizedvch
        self.isexcisemanufactureron = isexcisemanufactureron
        self.isblankcheque = isblankcheque
        self.isvoid = isvoid
        self.isonhold = isonhold
        self.orderlinestatus = orderlinestatus
        self.vatisagnstcancsales = vatisagnstcancsales
        self.vatispurcexempted = vatispurcexempted
        self.isvatrestaxinvoice = isvatrestaxinvoice
        self.vatisassesablecalcvch = vatisassesablecalcvch
        self.isvatdutypaid = isvatdutypaid
        self.isdeliverysameasconsignee = isdeliverysameasconsignee
        self.isdispatchsameasconsignor = isdispatchsameasconsignor
        self.isdeleted = isdeleted
        self.changevchmode = changevchmode
        self.alterid = alterid
        self.masterid = masterid
        self.voucherkey = voucherkey
        self.excludedtaxations_list = excludedtaxations_list
        self.oldauditentries_list = oldauditentries_list
        self.accountauditentries_list = accountauditentries_list
        self.auditentries_list = auditentries_list
        self.dutyheaddetails_list = dutyheaddetails_list
        self.supplementarydutyheaddetails_list = supplementarydutyheaddetails_list
        self.ewaybilldetails_list = ewaybilldetails_list
        self.invoicedelnotes_list = invoicedelnotes_list
        self.invoiceorderlist_list = invoiceorderlist_list
        self.invoiceindentlist_list = invoiceindentlist_list
        self.attendanceentries_list = attendanceentries_list
        self.originvoicedetails_list = originvoicedetails_list
        self.invoiceexportlist_list = invoiceexportlist_list
        self.allledgerentries_list = allledgerentries_list
        self.payrollmodeofpayment_list = payrollmodeofpayment_list
        self.attdrecords_list = attdrecords_list
        self.gstewayconsignoraddress_list = gstewayconsignoraddress_list
        self.gstewayconsigneeaddress_list = gstewayconsigneeaddress_list
        self.tempgstratedetails_list = tempgstratedetails_list
        self.remoteid = remoteid
        self.vchkey = vchkey
        self.vchtype = vchtype
        self.action = action
        self.objview = objview
        self.fbtpaymenttype = fbtpaymenttype
        self.address_list = address_list
        self.basicbuyeraddress_list = basicbuyeraddress_list
        self.basicorderterms_list = basicorderterms_list
        self.alteredon = alteredon
        self.statename = statename
        self.alteredby = alteredby
        self.countryofresidence = countryofresidence
        self.partygstin = partygstin
        self.partyname = partyname
        self.basicbasepartyname = basicbasepartyname
        self.typeofexcisevoucher = typeofexcisevoucher
        self.placeofsupply = placeofsupply
        self.consigneegstin = consigneegstin
        self.basicbuyername = basicbuyername
        self.basicduedateofpymt = basicduedateofpymt
        self.consigneepinnumber = consigneepinnumber
        self.consigneestatename = consigneestatename
        self.ledgerentries_list = ledgerentries_list
        self.allinventoryentries_list = allinventoryentries_list
        self.classname = classname
        self.consigneecstnumber = consigneecstnumber
        self.buyerscstnumber = buyerscstnumber
        self.basicdatetimeofinvoice = basicdatetimeofinvoice
        self.basicdatetimeofremoval = basicdatetimeofremoval
        self.gstregistrationtype = gstregistrationtype
        self.vatdealertype = vatdealertype
        self.buyeraddresstype = buyeraddresstype
        self.taxunitname = taxunitname


class XmlnsUDF(Enum):
    TALLY_UDF = "TallyUDF"


class Tallymessage:
    voucher: Voucher
    xmlns_udf: XmlnsUDF

    def __init__(self, voucher: Voucher, xmlns_udf: XmlnsUDF) -> None:
        self.voucher = voucher
        self.xmlns_udf = xmlns_udf


class Requestdata:
    tallymessage: List[Tallymessage]

    def __init__(self, tallymessage: List[Tallymessage]) -> None:
        self.tallymessage = tallymessage


class Staticvariables:
    svcurrentcompany: str

    def __init__(self, svcurrentcompany: str) -> None:
        self.svcurrentcompany = svcurrentcompany


class Requestdesc:
    reportname: str
    staticvariables: Staticvariables

    def __init__(self, reportname: str, staticvariables: Staticvariables) -> None:
        self.reportname = reportname
        self.staticvariables = staticvariables


class Importdata:
    requestdesc: Requestdesc
    requestdata: Requestdata

    def __init__(self, requestdesc: Requestdesc, requestdata: Requestdata) -> None:
        self.requestdesc = requestdesc
        self.requestdata = requestdata


class Body:
    importdata: Importdata

    def __init__(self, importdata: Importdata) -> None:
        self.importdata = importdata


class Header:
    tallyrequest: str

    def __init__(self, tallyrequest: str) -> None:
        self.tallyrequest = tallyrequest


class Envelope:
    header: Header
    body: Body

    def __init__(self, header: Header, body: Body) -> None:
        self.header = header
        self.body = body


class Welcome9:
    envelope: Envelope

    def __init__(self, envelope: Envelope) -> None:
        self.envelope = envelope
